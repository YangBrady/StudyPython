class Student(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器
    @property
    def name(self):
        return self.name()

    # 修改器
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self.age()

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

    # 静态方法
    @staticmethod
    def is_adult(self):
        if self._age >= 18:
            print(self._name + "是成年人")
        else:
            print(self._name + "不是成年人")


class Student2(object):
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self.name()

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self.age()

    @age.setter
    def age(self, age):
        self._age = age


def main():
    student = Student("JOJO", 10)
    student.play()
    student.age = 22
    student.play()

    Student.is_adult(student)

    # Python是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法
    student.foo = 1  # 不会报错，但是最好通过 __slots__魔法限定自定义类型的对象只能绑定某些属性

    # student2 = Student2("KOKO", 20)
    # student2.foo = 1  # 会报错


if __name__ == '__main__':
    main()
