import logging
import sys

from pyxmpp2.jid import JID
from pyxmpp2.client import Client
from pyxmpp2.settings import XMPPSettings
from pyxmpp2.interfaces import EventHandler, event_handler
from pyxmpp2.message import Message
from pyxmpp2.interfaces import XMPPFeatureHandler
from pyxmpp2.interfaces import message_stanza_handler

# (1) ログレベルを設定
logging.basicConfig(level = logging.DEBUG)

# (2) EventHandlerとXMPPFeatureHandlerを拡張したEchoBotHandlerクラスの実装
class EchoBotHandler(EventHandler, XMPPFeatureHandler):
    # (3) EventHandlerでイベントのログを採取
    @event_handler()
    def handle_all(self, event):
        logging.info("-- {0}".format(event))
        
    # (4) XMPPのメッセージを受信したときの処理を記述
    @message_stanza_handler()
    def handle_message(self, stanza):
        # (4-1)メッセージのタイトルを設定
        if stanza.subject:
            subject = "Re: " + stanza.subject
        else:
            subject = None

        if stanza.body:
            # (4-2)メッセージの本文の作成
            body = 'You said "' + stanza.body + '".'
            # (5) メッセージオブジェクトの作成
            msg = Message(stanza_type = stanza.stanza_type,
                        from_jid = stanza.to_jid, to_jid = stanza.from_jid,
                        subject = subject, body = body,
                        thread = stanza.thread)
            return msg

# (6) XMPPの初期化とイベントループ
jid = sys.argv[1]
password = sys.argv[2]
settings = XMPPSettings({ "password": password })
client = Client(JID(jid), [EchoBotHandler()], settings)
client.connect()

client.run()

