class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # 无法访问
    test.__bar()
    print(test.__foo)

    # 可以访问，但是不建议这么做
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
