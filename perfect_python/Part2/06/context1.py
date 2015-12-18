import io
class SpamContext:
    def __enter__(self):
        self.save = __builtins__.open
        __builtins__.open = lambda *args:io.StringIO("spam")

    def __exit__(self, exc_type, exc_value, traceback):
       __builtins__.open = self.save

with SpamContext():
    print(open("./test.txt").read())
    print(open("./test2.txt").read())

