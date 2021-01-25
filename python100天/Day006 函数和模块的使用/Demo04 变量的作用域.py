def foo():
    b = 'hello'  # 局部变量（local variable），属于局部作用域

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print("a=", a)
        print("b=", b)
        print("c=", c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


# 修改全局变量的方法
def foo1():
    a = 200  # 这样是无法修改全局变量a的


def foo2():
    """
    global关键字来指示foo函数中的变量a来自于全局作用域，如果全局作用域中没有a，那么下面一行的代码就会定义变量a并将其置于全局作用域。
    如果我们希望函数内部的函数能够修改嵌套作用域中的变量，可以使用nonlocal关键字来指示变量来自于嵌套作用域
    """
    global a
    a = 200  # 修改全局变量a


if __name__ == '__main__':
    a = 100  # 全局变量（global variable），属于全局作用域，没有定义在任何一个函数中
    # print(b)  # NameError: name 'b' is not defined
    foo()
    foo1()
    # foo2()
    print("a=", a)
