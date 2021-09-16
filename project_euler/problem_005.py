"""             Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
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
