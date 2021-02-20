import sys


def main():
    # pass
    # list_define()
    # list_loop()
    # list_add_remove()
    list_cut()
    # list_sort()
    # list_gen()


def list_define():
    list1 = [1, 3, 5, 7, 100]
    print("list1=", list1)  # [1, 3, 5, 7, 100]

    # 乘号表示列表元素的重复
    list2 = ['hello'] * 3
    print("list2=", list2)  # ['hello', 'hello', 'hello']

    # 计算列表长度(元素个数)
    print(len(list1))  # 5

    # 下标(索引)运算
    print(list1[0])  # 1
    # print(list1[5])  # IndexError: list index out of range
    print(list1[-1])  # 100
    print(list1[-3])  # 5
    list1[2] = 300
    print("list1=", list1)  # [1, 3, 300, 7, 100]


# 遍历list
def list_loop():
    list1 = [1, 3, 5, 7, 100]

    def range_loop():
        # 通过循环用下标遍历列表元素
        for index in range(len(list1)):
            print(list1[index])

    def for_loop():
        # 通过for循环遍历列表元素
        for elem in list1:
            print(elem)

    def enumerate_loop():
        # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
        for index, elem in enumerate(list1):
            print(index, elem, sep=" -> ")

    enumerate_loop()


# 增删元素
def list_add_remove():
    list1 = [1, 3, 5, 7, 100]
    # 添加元素
    list1.append(200)
    list1.insert(1, 400)
    # 合并两个列表
    # list1.extend([1000, 2000])
    list1 += [1000, 2000]
    print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
    print(len(list1))  # 9
    # 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
    if 3 in list1:
        list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)
    print(list1)  # [1, 400, 5, 7, 100, 200, 1000, 2000]
    # 从指定的位置删除元素
    list1.pop(0)
    list1.pop(len(list1) - 1)
    print(list1)  # [400, 5, 7, 100, 200, 1000]
    # 清空列表元素
    list1.clear()
    print(list1)  # []


# 列表分片，字符串也可以进行切片操作
def list_cut():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 列表分片
    fruits2 = fruits[1:4]  # 前闭后开区间
    print(fruits2)  # apple strawberry waxberry
    # 可以通过完整分片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    fruits4 = fruits[-3:-1]
    print(fruits4)  # ['pitaya', 'pear']
    # 每隔2个取一个
    fruits5 = fruits[::2]
    print(fruits5)  # ['grape', 'strawberry', 'pitaya', 'mango']
    # 可以通过反向分片操作来获得倒转后的列表的拷贝
    fruits6 = fruits[::-1]
    print(fruits6)  # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']


# 列表排序
def list_sort():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用

    list3 = sorted(list1, reverse=True)

    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)

    print("list1=", list1)
    print("list2=", list2)
    print("list3=", list3)
    print("list4=", list4)

    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print("list1=", list1)


# 生成式和生成器，一个式中括号一个式小括号
def list_gen():
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x for x in range(1, 10)]
    print("f=", f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print("f=", f)
    f = [x ** 2 for x in range(1, 10)]  # **表示乘方
    print("f占用内存的字节数", sys.getsizeof(f))
    print("f=", f)

    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 10))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print("f=", f)
    for val in f:
        print(val)


if __name__ == '__main__':
    main()
