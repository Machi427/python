var1 = 'グローバル' # グローバル変数

def spam():
    var2 = 'ローカル' # ローカル変数
    return (var1, var2)


if __name__ == '__main__':
    print(spam())
