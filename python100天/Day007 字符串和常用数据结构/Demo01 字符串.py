def main():
    # pass
    string_define()
    string_operation()


# 字符串使用
def string_define():
    s1 = 'hello, world!'
    s2 = "hello, world!"
    # 以三个双引号或单引号开头的字符串可以折行
    s3 = """
    hello, 
    world!
    """
    print(s1, s2, s3, end='')

    """
    \n 换行
    \t 制表符
    \\ \
    """
    print("\n-----转义-----\n")
    s1 = '\'hello, world!\''
    s2 = '\n\\hello, world!\\\n'
    print(s1, s2, end='')

    print("\n----------\n")
    s1 = '\141\142\143\x61\x62\x63'
    s2 = '\u6768\u5cfb'
    print(s1, s2)

    print("\n-----禁止转义-----\n")
    s1 = r'\'hello, world!\''
    s2 = r'\n\\hello, world!\\\n'
    print(s1, s2, end='')


# 字符串运算
def string_operation():
    s1 = 'hello ' * 3
    print("s1=", s1)  # hello hello hello
    s2 = 'world'
    s1 += s2
    print("s1=", s1)  # hello hello hello world
    print('ll' in s1)  # True
    print('good' in s1)  # False

    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print("str2指定位置：", str2[2])  # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45


def string_function():
    str1 = 'hello, world!'
    # 通过内置函数len计算字符串的长度
    print(len(str1))  # 13
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())  # Hello, world!
    # 获得字符串每个单词首字母大写的拷贝
    print(str1.title())  # Hello, World!
    # 获得字符串变大写后的拷贝
    print(str1.upper())  # HELLO, WORLD!
    # 从字符串中查找子串所在位置
    print(str1.find('or'))  # 8
    print(str1.find('shit'))  # -1
    # 与find类似但找不到子串时会引发异常
    # print(str1.index('or'))
    # print(str1.index('shit'))
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('He'))  # False
    print(str1.startswith('hel'))  # True
    # 检查字符串是否以指定的字符串结尾
    print(str1.endswith('!'))  # True
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))
    str2 = 'abc123456'
    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False
    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())  # True
    str3 = '  jackfrued@126.com '
    print(str3)
    # 获得字符串修剪左右两侧空格之后的拷贝
    print(str3.strip())

    # 格式化输出
    a, b = 5, 10
    print('{0} * {1} = {2}'.format(a, b, a * b))  # 格式化输出
    print(f'{a} * {b} = {a * b}')  # Python 3.6+


if __name__ == '__main__':
    main()
