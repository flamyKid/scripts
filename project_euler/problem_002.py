"""             Четные числа Фибоначчи
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""


def even_fibonacci_numbers(max_limit):
    result_list = list()
    fibonacci_nums_list = [1, 2]

    for i in fibonacci_nums_list:
        if i >= max_limit:
            break
        next_num = fibonacci_nums_list[-2] + fibonacci_nums_list[-1]
        fibonacci_nums_list.append(next_num)

    for i in fibonacci_nums_list:
        if i % 2 == 0:
            result_list.append(i)

    return sum(result_list)


if __name__ == '__main__':
    print(even_fibonacci_numbers(4000000))  # output: 4613732
