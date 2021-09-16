import math
def func(num_load):
    l = list()
    r = math.ceil(math.sqrt(num_load))
    for num in range(3, r):
        x = num_load / num
        if num_load % num == 0:
            l.append(x)
    return l


# тестирование функции
print(max(func(600851475143)))
