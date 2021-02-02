class Test:
    def __init__(self, foo, koo):
        self.__foo = foo  # 私有
        self._koo = koo  # 受保护，python中一般建议属性定义成受保护的

    def __bar(self):  # 私有
        print(self.__foo)
        print('__bar')

    def bar2(self):
        print(self._koo)
        print('_bar2')

    @property
    def koo(self):
        return self._koo


def main():
    test = Test('hello', 'world')
    print(test.koo)

    # 无法访问
    test.__bar()
    print(test.__foo)

    # 可以换一种方式直接访问私有属性或者方法，但是不建议这么做
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
