import random


def game_ai():
    ai_sign = random.choice(['rock', 'scissors', 'paper'])

    return ai_sign


def game(user_sign, ai_sign, username):
    if user_sign == 'rock' and ai_sign == 'scissors' or \
            user_sign == 'paper' and ai_sign == 'rock' or \
            user_sign == 'scissors' and ai_sign == 'paper':
        return f'{username} is winner!'
    elif ai_sign == 'rock' and user_sign == 'scissors' or \
            ai_sign == 'paper' and user_sign == 'rock' or \
            ai_sign == 'scissors' and user_sign == 'paper':
        return 'AI is winner'
    else:
        return 'A tie!'


def main(username):
    user_sign = input('Pick(rock, scissors, paper):')
    ai_sign = game_ai()
    print(f'You have chosen: {user_sign}')
    print(f'AI chose: {ai_sign}')

    result = game(user_sign, ai_sign, username)

    return result


if __name__ == '__main__':
    print('"Rock, scissors, paper"')

    username = input('Who you are: ')

    while True:
        answer = input('Want to play(y or n)?')

        if answer == 'y':
            result = main(username)
            print(result)
            print('')
        else:
            break
