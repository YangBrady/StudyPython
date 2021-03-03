def main():
    # pass
    # set_define()
    # set_add_remove()
    set_calculate()


def set_define():
    # 定义一个空set
    set_null = set()
    # 创建集合的字面量语法
    set1 = {1, 2, 3, 3, 3, 2}
    print("set1 =", set1)
    print('set1 length =', len(set1))

    # 创建集合的构造器语法(面向对象部分会进行详细讲解)
    set2 = set(range(1, 10))
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set2, set3)
    # 创建集合的推导式语法(推导式也可以用于推导集合)
    set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
    print("set4 =", set4)


def set_add_remove():
    set1 = {1, 2, 3, 3, 3, 2}
    set1.add(4)
    set1.add(5)

    set2 = set(range(1, 10))
    set2.update([11, 12])
    set2.discard(5)
    if 4 in set2:
        set2.remove(4)
    print(set1, set2)

    set3 = {1, 2, 3}
    print(set3.pop())  # pop() 方法用于随机移除一个元素
    print("set3 =", set3)


def set_calculate():
    set1 = {0, 1, 2, 3}
    set2 = set(range(1, 10))
    set3 = {1, 2, 3}
    # 集合的交集、并集、差集、对称差运算
    print(set1 & set2)  # print(set1.intersection(set2))
    print(set1 | set2)  # print(set1.union(set2))
    print(set1 - set2)  # print(set1.difference(set2))
    print(set1 ^ set2)  # print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print(set2 <= set1)  # print(set2.issubset(set1))
    print(set3 <= set1)  # print(set3.issubset(set1))
    print(set1 >= set2)  # print(set1.issuperset(set2))
    print(set1 >= set3)  # print(set1.issuperset(set3))


if __name__ == '__main__':
    main()
