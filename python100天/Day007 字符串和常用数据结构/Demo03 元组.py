def main():
    # pass
    use_tuples()


# 元组中的元素是无法修改
def use_tuples():
    # 定义元组
    t = ('派大星', 100, True, '广东深圳')
    print("t=", t)

    # 获取元组中的元素
    print("t[0]=", t[0])
    print("t[3]=", t[3])

    # 遍历元组中的值
    for member in t:
        print(member)

    # 重新给元组赋值
    # t[0] = '王大锤'  # Tuples don't support item assignment
    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print("t=", t)

    # 将元组转换成列表
    person = list(t)
    print("person=", person)
    # 列表是可以修改它的元素的
    person[0] = '李小龙'
    person[1] = 25
    print("person=", person)

    # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print("fruits_tuple=", fruits_tuple)


if __name__ == '__main__':
    main()
