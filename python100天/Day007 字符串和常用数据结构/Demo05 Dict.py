def main():
    # pass
    use_dict()


def use_dict():
    # 创建字典的字面量语法
    scores = {'小明': 99, '白元芳': 78, '狄仁杰': 82}
    print("scores =", scores)

    # 创建字典的构造器语法
    items1 = dict(one=1, two=2, three=3, four=4)

    # 通过zip函数将两个序列压成字典
    items2 = dict(zip(['a', 'b', 'c'], '123'))

    # 创建字典的推导式语法
    items3 = {num: num ** 2 for num in range(1, 10)}
    print(items1, items2, items3)

    # 通过键可以获取字典中对应的值
    print(scores['小明'])
    print(scores.get('小明'))
    print(scores.get('小天', 89))  # 不存在的话返回默认值

    # 对字典中所有键值对进行遍历
    for key in scores:
        print(f'{key}: {scores[key]}')
    # 更新字典中的元素
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print("scores =", scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))

    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('小明', 100))

    # 清空字典
    scores.clear()
    print("scores =", scores)


if __name__ == '__main__':
    main()
