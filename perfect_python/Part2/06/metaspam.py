class MetaSpam(type):
    def __new__(metacls, name, bases, classdict, num_spam):
        return type.__new__(metacls, name, bases, classdict)

    def __init__(cls, name, bases, classdict, num_spam):
        type.__init__(cls, name, bases, classdict)
        cls.spam = num_spam

class Spam(metaclass=MetaSpam, num_spam=100):
    pass

print(Spam().spam)      # 100が出力される 

