import numpy as np


def main():
    # pass
    test5()


def test1():
    n = 1234567890.123456789012345
    "{:.9e}".format(n)
    print(n)


def test2():
    a = np.array([2, 4, 6, 8, 10])
    b = np.where(a > 5, None)  # 返回索引
    print(b)


def test3():
    for a in range[0, 10]:
        b += a
        print(a)


def test4():
    foo4_1("aaa")


def foo4_1(a):
    foo4_1(a, "123")


def foo4_1(a, b):
    print(a)
    print(b)


def test5():
    a, b = test5_1()
    print(a)
    print(b)


def test5_1():
    return "123", 18


if __name__ == '__main__':
    main()
