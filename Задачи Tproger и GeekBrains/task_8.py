# 19.04.2020
def is_palindrom(string):
    if string == string[::-1]:
        print('это строка палиндром!')

is_palindrom('abba')