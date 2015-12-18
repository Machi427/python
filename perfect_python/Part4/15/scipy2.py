from scipy import integrate

def echo(x):
    ''' 受け取った値をそのまま返す関数 '''
    return x

# 受け取った値をそのまま返す関数を 0 から 10 の区間で積分
result, error = integrate.quad(echo, 0, 10)

# 結果
print(result) #=> 50.0

# 誤差
print(error) #=> 5.551115123125783e-13

