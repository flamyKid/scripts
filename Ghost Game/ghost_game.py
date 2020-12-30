from random import randint
import time

print('---Ghost House---')
print('________________')

while True:
    def ghost_game():
        life = 1
        score = 0
        feeling_brave = True

        while feeling_brave:
            ghost_door = randint(1, 3)
            print('You see 3 doors...')
            print ('There\'s a ghost in one of them.')
            print ('Which one will you open?')
            door = input('1, 2, или 3?')
            if door == 'life+=1':  # secret command
                life += 1
                print('life:', life)
            else:
                door_num = int(door)
                if door_num == ghost_door:
                    print('______')
                    print('GHOST!')
                    life = life - 1
                    if life == 0:
                        feeling_brave = False
                    else:
                        print('You used the extra life')
                        print('Remaining:', life)
                        print('Your glasses', score)
                else:
                    print('No ghost!')
                    print('Keep going.')
                    score = score + 1
                    time.sleep(1.5)
                    print('________________')
        print('Run, men!')
        print('Yours score:', score)
    ghost_game()
    answer = input('Want to start the game again? Enter \'y\' or \'n\')
    if answer == 'y':
        ghost_game()
    else:
        break
