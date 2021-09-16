"""             Наименьшее кратное
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""


def smallest_multiple(start_num, limit_num):
    num = 0
    length = limit_num - start_num

    while True:
        divider = 0
        num += 1

        for i in range(start_num, limit_num):
            if num % i == 0:
                divider += 1

        if divider == length:
            return num


if __name__ == '__main__':
    print(smallest_multiple(1, 21))  # output: 232792560
