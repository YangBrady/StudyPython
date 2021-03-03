"""
生成get和set方法
"""


class ClassName:
    # def __init__(self):
    #     self._link_East = []
    #     self._link_South = []
    #     self._link_West = []
    #     self._link_North = []
    # def __init__(self):
    #     self.__link_East = []
    #     self.__link_South = []
    #     self.__link_West = []
    #     self.__link_North = []
    def __init__(self):
        self.__upLane = []
        self.__downLane = []

def foo1():
    clazz = ClassName()
    for k in clazz.__dict__:
        if k.startswith('_ClassName__'):
            param_split = '__'
            param_name = k[12:]
        elif k.startswith('_'):
            param_split = '_'
            param_name = k[1:]

        print("@property")
        print("def " + param_name + "(self):")
        print("\treturn self." + param_split + param_name)
        print("@" + param_name + ".setter")
        print("def " + param_name + "(self," + param_name + "):")
        print("\tself." + param_split + param_name + " = " + param_name)
        print("\t")


if __name__ == '__main__':
    foo1()
