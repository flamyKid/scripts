num = list(range(0, 1000)) # список с числами от 0 до 1000
result = list() # список с числами которые делятся на 3 и 5

print(list([elem for elem in num if elem%3==0 and elem%5==0]))
