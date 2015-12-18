#!/usr/bin/env python

"""
(1) lurklibライブラリのインポート
"""
import lurklib

class Bot(lurklib.Client):
    """
    (2) Botクラス。IRCからのイベントをハンドリングするために、
    lucklib.Clientの派生クラスを作成します
    """
    
    def on_connect(self):
        """
        (3) on_connectメソッドはIRCのネットワークに接続したときに呼び出されます。
        ここでは、#perfect_python_botと言うチャネルに接続します。
        """
        print("connected")
        self.join_('#perfect_python_bot')

    def on_join(self, from_, channel):
        """
        (4) on_joinはチャネルに参加が完了したときに呼び出されます。
        """
        print("joined")
        
    def on_chanmsg(self, from_, channel, message):
        """
        (5) on_chanmsgはチャネル(channel)宛のメッセージを受信したとき
        呼び出されます。
        ここでは、messageが"hello"だった場合、
        botがチャネル宛てに返事をします。
        """
        print("# channel: " + channel)
        print("# message:" + message)
        if message == 'hello':
            print('%s said hello!' % from_[0])
            self.privmsg(channel, 'Hello, %s!' % from_[0])


if __name__ == '__main__':
    """
    (6) Botのオブジェクトを作成します。
    irc.freenode.netのサーバに
    ニックネームPPythonBot,ユーザIDPPythonBot-で接続します。
    """
    bot = Bot(server="irc.freenode.net",
              nick="PPythonBot", user='PPythonBot-')

    """
    (7) lurklibのイベントループを実行します。
    IRCサーバと切断されるまでブロックします。
    """
    bot.mainloop()

