from random import randint


print('___Дом с приведениями___')

score = 0
feeling_brave = True

while feeling_brave:
    ghost_door = randint(1, 3)
    print('Ты видишь 3 двери...')
    print ('В одной из них призрак.')
    print ('Какую ты откроешь?')
    door = input('1, 2, или 3?')

    if int(door) == ghost_door:
        feeling_brave = False
    else:
        print('Нет призрака!')
        print('Можешь идти дальше.')
        score = score + 1
    print('_________')
print('Призрак! Беги!')
print('Твои очки:', score)
