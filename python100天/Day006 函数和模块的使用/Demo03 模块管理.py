from module1 import foo

foo()  # 输出hello

from module2 import foo

# 如果导入的模块除了定义函数之外还中有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码
foo()  # 输出goodbye, world!

from module3 import foo
foo()  # 输出goodbye, world!
