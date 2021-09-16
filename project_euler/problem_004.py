"""             Наибольшее произведение-палиндром
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""


def largest_palindrome_product(start_num, limit_num):
    nums = []

    for i in range(start_num, limit_num)[::-1]:
        for j in range(start_num, limit_num)[::-1]:
            if str(i * j) == str(i * j)[::-1]:
                nums.append(i * j)

    return max(nums)


if __name__ == '__main__':
    print(largest_palindrome_product(100, 1000))  # output: 906609
