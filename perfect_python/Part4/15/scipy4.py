from scipy import integrate

def func(x):
    print(x)
    return x


# 中で print 関数を呼んでいる関数を積分してみる
integrate.quad(func, 0, 10)

