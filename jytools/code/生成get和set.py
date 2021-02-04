"""
生成get和set方法
"""


class ClassName:
    def __init__(self):
        self._link_East = []
        self._link_South = []
        self._link_West = []
        self._link_North = []


if __name__ == '__main__':
    clazz = ClassName()
    # print(clazz.__dict__)
    for k in clazz.__dict__:
        if k.startswith('_'):
            param = k[1:]

        print("@property")
        print("def " + param + "(self):")
        print("\treturn self._" + param)

        print("@" + param + ".setter")
        print("def " + param + "(self," + param + "):")
        print("\tself._" + param + " = " + param)
