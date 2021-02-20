from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


def main():
    day1 = Weekday.Mon
    print(day1)  # Weekday.Mon


if __name__ == '__main__':
    main()
