from scipy import integrate

def ret1(x):
    ''' 常に 1 を返す関数 '''
    return 1

# 常に 1 を返す関数を 0 から 10 の区間で積分
result, error = integrate.quad(ret1, 0, 10)

# 積分した結果
print(result) #=> 10

# 計算誤差
print(error) #=> 1.1102230246251565e-13

