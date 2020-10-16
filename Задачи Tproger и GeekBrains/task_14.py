# 19.04.2020
def num2_for_lst(lst):
    for num in lst:
        if num == 237:
            break
        if num % 2 == 0:
            print(num)

num2_for_lst(range(0, 300))