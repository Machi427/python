import unittest
from unittest import mock
from ppjp.chat.client import EchoClient

class EchoClientTests(unittest.TestCase):
    def test_init(self):
        EchoClient.create_socket = mock.Mock()
        EchoClient.bind_all = mock.Mock()
        
        mock_view = mock.Mock()
        result = EchoClient(mock_view)

        self.assertEqual(result.view, mock_view)
        self.assertEqual(result.buffers, [])
        EchoClient.create_socket.assert_called_with()
        EchoClient.bind_all.assert_called_with()

    def test_bind_all(self):
        mock_target = mock.Mock()

        EchoClient.bind_all(mock_target)

        mock_target.view.entry.bind.assert_called_with('<Return>', mock_target.on_submit)

    def test_on_submit(self):
        mock_target = mock.Mock()
        mock_target.view.get_submit_messegae.return_value = 'test-data'
        mock_target.buffers = []

        EchoClient.on_submit(mock_target, mock.Mock())

        self.assertEqual(mock_target.buffers, [b'test-data'])

    def test_handle_write_with_empty(self):
        mock_target = mock.Mock()
        mock_target.buffers = []
        
        EchoClient.handle_write(mock_target)

        self.assertFalse(mock_target.send.called)
    
    def test_handle_write(self):
        mock_target = mock.Mock()
        mock_target.buffers = [b'a', b'b']

        EchoClient.handle_write(mock_target)

        self.assertEqual(mock_target.buffers, [b'b'])        
        mock_target.send.assert_called_with(b'a')

    def test_writable_with_empty(self):
        mock_target = mock.Mock()
        mock_target.buffers = []

        result = EchoClient.writable(mock_target)

        self.assertIs(result, False)

    def test_writable(self):
        mock_target = mock.Mock()
        mock_target.buffers = ['a']

        result = EchoClient.writable(mock_target)

        self.assertIs(result, True)
        
    def test_handle_reade(self):
        mock_target = mock.Mock()
        mock_target.recv.return_value = b'test'

        EchoClient.handle_read(mock_target)

        mock_target.recv.assert_called_with(8192)
        mock_target.view.show_message.assert_called_with('test')
