from urllib.request import Request
from urllib.request import HTTPPasswordMgrWithDefaultRealm
from urllib.request import HTTPBasicAuthHandler
from urllib.request import build_opener
from urllib.request import install_opener
from urllib.request import urlopen

req = Request("http://example.com/")

password_manager = HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, "http://example.com/", 'user', 'pass')
auth_manager = HTTPBasicAuthHandler(password_manager)
opener = build_opener(auth_manager)
install_opener(opener)

handler = urlopen(req)

print(handler.getcode())

