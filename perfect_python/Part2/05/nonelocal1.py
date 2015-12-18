def outer():
    var1 = '外側の変数'
    
    def inner():
        var2 = '内側の変数'
        return (var1, var2)
    
    return inner()


if __name__ == '__main__':
    print(outer())

