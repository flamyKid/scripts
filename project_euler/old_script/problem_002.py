def func(num, numfi):
    result = list()  # список с четными числами фибоначи
    last_num = 2 # предыдущее число из списка num
    last_index = 0 # индекс прошлого числа в списке num
    for elem in num:
        while True:
            if last_num >= 4000000:
                break
            last_num = int(numfi[last_index]) + last_num # сумма 2-х предыдущих чисел
            numfi.append(last_num) # добавление суммы в список фибоначи
            last_index += 1

    for elem in numfi:  # отбор четных чисел фибоначи
        if elem%2==0:
            result.append(elem)
    print(sum(result)) # сумма четных чисел фибоначи


# тестирование функции
num = list(range(1, 4000000)) # создание картежа с числами
numfi = list([1, 2]) # создание списка с числами фибоначи
func(num, numfi)
