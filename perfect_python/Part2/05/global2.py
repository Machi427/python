var1 = 'グローバル' # グローバル変数

def spam():
    global var1   # var1をグローバル変数と宣言し、
                  # 値を変更できるようにする
    var1 = 'ローカルで変更'   # グローバル変数を更新
    var2 = 'ローカル'         # ローカル変数
    return (var1, var2)


if __name__ == '__main__':
    print(spam())

