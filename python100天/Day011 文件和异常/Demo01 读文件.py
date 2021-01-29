def main():
    # read_file()
    # read_file1()
    # read_file2()
    read_line()
    # pass


# 一次性读取整个文件内容
def read_file():
    # f = open('testFiles/Nodes.csv', 'r', encoding='utf-8')
    f = open('testFiles/Nodes.csv2', 'r', encoding='utf-8')
    print(f.read())
    f.close()


def read_file1():
    f = None
    try:
        f = open('testFiles/Nodes.csv', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


def read_file2():
    try:
        with open('testFiles/Nodes.csv', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


def read_line():
    # 通过for-in循环逐行读取
    # with open('testFiles/Nodes.csv', mode='r') as f:
    #     for line in f:
    #         print(line, end='')
    # print()

    # 读取文件按行读取到列表中
    with open('testFiles/movement.csv') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
