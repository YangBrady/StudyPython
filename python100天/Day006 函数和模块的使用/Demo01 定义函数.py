# 求阶乘
def fac(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


# 可以返回多个值
def fac2():
    arg1 = 1
    arg2 = 2
    return arg1, arg2


m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m - n))

a, b = fac2()
print(f"a={a}, b={b}")
