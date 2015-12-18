def outer():
    var1 = '外側の変数'
    var2 = 'これも外側の変数'

    def inner():
        nonlocal var1    # var1を外側の関数の変数と宣言し、
                         # 値を変更できるようにする
        var1 = '内側で変更'  # outer() の var1 を更新
        var3 = '内側の変数'
        return (var1, var2, var3)
    
    return inner()


if __name__ == '__main__':
    print(outer())

