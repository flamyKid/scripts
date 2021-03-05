# это моя первая самостоятельная программа. Написал 3(или 5) января 2019 года.
while True:
    print('Опции:')
    print('add - операция сложения')
    print('subtract - операция вычитания')
    print('multiply - операция умножения')
    print('divide - операция деления')
    print('stop - остановка программы')
    user_input = input('>>>')
    if user_input == 'stop':
        break
    elif user_input == 'add':
        num1 = float(input('Первое слагаемое:'))
        num2 = float(input('Второе слагаемое:'))
        result = str(num1 + num2)
        print('Ответ:', result)
    elif user_input == 'subtract':
        num1 = float(input('Уменьшаемое:'))
        num2 = float(input('Вычитаемое:'))
        result = str(num1 - num2)
        print('Ответ:', result)
    elif user_input == 'multiply':
        num1 = float(input('Первый множитель:'))
        num2 = float(input('Второй множитель:'))
        result = str(num1 * num2)
        print('Ответ:', result)
    elif user_input == 'divide':
        num1 = float(input('Делимое:'))
        num2 = float(input('Делитель:'))
        result = str(num1 / num2)
        print('Ответ:', result)
    else:
        print('Введите команду')
