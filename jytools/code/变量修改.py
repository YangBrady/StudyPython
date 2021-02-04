# 驼峰转下划线
def get_lower_case_name(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)

    return "".join(lst).lower()


if __name__ == '__main__':
    print(get_lower_case_name("linkEast"))
    print(get_lower_case_name("linkSouth"))
    print(get_lower_case_name("linkWest"))
    print(get_lower_case_name("linkNorth"))
