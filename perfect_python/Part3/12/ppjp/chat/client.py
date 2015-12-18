# -*- coding::utf-8 -*-

import tkinter
import asyncore
import functools

class EchoView(tkinter.Frame):
    """ Echo User Interface """

    def __init__(self, master):
        super(EchoView, self).__init__(master)
        self.listcontainer = tkinter.Frame(self)
        self.listbox = tkinter.Listbox(self.listcontainer)
        self.yscroll = tkinter.Scrollbar(self.listcontainer)
        self.listbox.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)
        self.yscroll.pack(side=tkinter.LEFT, expand=True, fill=tkinter.Y)
        self.listcontainer.pack(expand=True, fill=tkinter.BOTH)

        self.entry = tkinter.Entry(self)
        self.entry.pack(side=tkinter.BOTTOM, expand=True, fill=tkinter.X)

    def get_submit_messegae(self):
        data = self.entry.get()
        self.entry.delete(0, tkinter.END)
        return data

    def show_message(self, message):
        self.listbox.insert(tkinter.END, message)
        self.listbox.see(tkinter.END)
        
class EchoClient(asyncore.dispatcher_with_send):
    def __init__(self, view):
        super(EchoClient, self).__init__()
        self.create_socket()
        self.buffers = []
        self.view = view
        self.bind_all()

    def bind_all(self):
        self.view.entry.bind('<Return>', self.on_submit)

    def on_submit(self, event):
        message = self.view.get_submit_messegae()
        self.buffers.append(message.encode('utf-8'))

    def handle_write(self):
        if not self.buffers:
            return
        buffer, self.buffers = self.buffers[0],self.buffers[1:]
        self.send(buffer)

    def writable(self):
        return self.buffers


    def handle_read(self):
        message = self.recv(8192)
        self.view.show_message(message.decode('utf-8'))

def idle_task(root):
    try:
        asyncore.loop(count=1, timeout=1)
    finally:
        root.after(200, functools.partial(idle_task, root))

def main():
    root = tkinter.Tk()
    root.after(200, functools.partial(idle_task, root))
    view = EchoView(root)
    view.pack(expand=True, fill=tkinter.BOTH)
    client = EchoClient(view)
    client.connect(('localhost', 8080))
    root.mainloop()

if __name__ == '__main__':
    main()
