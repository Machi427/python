import sys
import os
import imp
import http.client
from urllib import parse

EXTENTION = '.txt'

def _create_full_path(path, fullname):
    """インターネットのパスを生成するヘルパー関数。
    ※ファインダ・ローダーの本質では有りません。"""
    url_component = parse.urlparse(path)
    target = url_component.scheme + '://' + url_component.netloc \
             + os.path.join(os.path.normpath(url_component.path), \
             *(fullname.split('.'))) + EXTENTION
    return target

def _package_path(path, fullname):
    """インターネットのパッケージパスを生成するヘルパー関数。
    ※ファインダ・ローダーの本質では有りません。"""
    target = _create_full_path(path, fullname)
    res = os.path.dirname(target) + '/{0}/__init__'.format(fullname) + EXTENTION
    return res

def _exist_url(target):
    """指定されたパスがインターネット上に存在するか確認するヘルパー関数
    ※ファインダ・ローダーの本質では有りません。"""
    url_component = parse.urlparse(target)
    conn = http.client.HTTPConnection(url_component.netloc)
    conn.request("HEAD", url_component.path)
    res = conn.getresponse()
    if __debug__:
      print('{0}: {1}'.format(res.status, target))
    if 200 <= res.status < 400:
        return True
    return False

def is_package(path, fullname):
    """指定されたパスがパッケージとしての形式でインターネット上に存在するか確認するヘルパー関数
    ※ファインダ・ローダーの本質では有りません。"""
    return _exist_url(_package_path(path, fullname))

class HttpImportFinder(object):
    """ファインダのサンプルクラス"""

    EXTENTION = '.txt'

    def __init__(self, path_entry):
        """sys.path_hooks に設定された場合、sys.pathの各エントリがpath_entryに入って呼び出されます"""
        self.path_entry = path_entry
        if path_entry.index('http://') != 0:
            raise ImportError() #扱えない場合には ImportError を送出します
        return #コンストラクタは値を返せませんので、呼び出し可能オブジェクトが値を返す事は期待されません
    
    def find_module(self, fullname, path=None):
        """fullname のパッケージやモジュールを見つけたらローダーを返すメソッド"""
        if is_package(self.path_entry, fullname):
            #指定されたパッケージを見つけたらローダーを返します
            return HttpImportLoader(self.path_entry)
        target = _create_full_path(self.path_entry, fullname)
        if _exist_url(target):
            #指定されたモジュールを見つけたらローダーを返します
            return HttpImportLoader(self.path_entry)
        return None #パッケージ・モジュールを見つけられない場合には None を返します

class HttpImportLoader(object):
    """ローダーのサンプルクラス"""

    def __init__(self, path):
        """ファインダの find_module でファインダのコンストラクタに渡されたパスを渡されて呼び出されます"""
        self.path_entry = path

    def load_module(self, fullname):
        """モジュールをロードするメソッド"""
        if fullname in sys.modules:
            #sys.modules に同じ名前があったら、再利用しなければなりません
            mod = sys.modules[fullname]
        else :
            #モジュールをロードする前に必ず sys.modules に追加します
            mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        if is_package(self.path_entry, fullname):
            target = _package_path(self.path_entry, fullname)
            #パッケージの場合にはパスを設定します。サブモジュールはこのパスを起点にして探索・インポートされます
            mod.__path__ = [self.path_entry]
            mod.__package__ = fullname #自分自身です
        else :
            target = _create_full_path(self.path_entry, fullname)
            #モジュールの場合、自分自身のパスを設定します
            mod.__path__ = _create_full_path(self.path_entry, fullname)
            mod.__package__ = '.'.join(fullname.split('.')[:-1]) #親の名前を設定します
        mod.__file__ = target
        mod.__name__ = fullname
        mod.__loader__ = self
        code = self.get_source(fullname)
        exec(code, mod.__dict__)
        return mod

    def get_source(self, fullname):
        """ソースコードを返すメソッド。定義しなくても構いません"""
        if is_package(self.path_entry, fullname):
            target = _package_path(self.path_entry, fullname)
        else :
            target = _create_full_path(self.path_entry, fullname)
        url_component = parse.urlparse(target)
        conn = http.client.HTTPConnection(url_component.netloc)
        conn.request("GET", url_component.path)
        res = conn.getresponse()
        code = res.read()
        return code

    def get_code(self, fullname):
        """コードオブジェクトを返すメソッド。定義しなくても構いません"""
        source = self.get_source(fullname)
        return compile(source, fullname, 'exec', dont_inherit=True)

    def is_package(self, fullname):
        """パッケージか否かを返すメソッド。定義しなくても構いません"""
        return is_package(self.path_entry, fullname)

    def get_filename(self, filename):
        """ファイル名を返すメソッド。定義しなくても構いません"""
        if is_package(self.path_entry, fullname):
            return _package_path(self.path_entry, fullname)
        else:
            return _create_full_path(self.path_entry, fullname)


'''以下のような構成でインターネットにファイルがあるとします。
http://static.tsuyukimakoto.com/mtsuyuki/__init__.txt
http://static.tsuyukimakoto.com/mtsuyuki/samp.txt

__init__.txt は空のファイル、 samp.txt には hello という関数定義が有るとします。'''

sys.path_hooks.append(HttpImportFinder) #sys.path_hooksに HttpImportFinder を登録します。
sys.path.append('http://static.tsuyukimakoto.com/') #sys.pathに起点の URL を登録します。

from mtsuyuki import samp #http経由でインポートして
print(samp.hello()) #インポートしたモジュールの関数を利用します

