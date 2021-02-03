from tkinter import *
import random


root = Tk()
root.title('Tic Tac Toe')

start_text = ' '
background = 'white'


game_run = True
field = []
cross_count = 0


def new_game():
    global game_run, cross_count

    for row in range(3):
        for column in range(3):
            field[row][column]['text'] = start_text
            field[row][column]['background'] = background

    game_run = True
    cross_count = 0


def click(row, column):
    global cross_count

    if game_run and field[row][column]['text'] == start_text:
        field[row][column]['text'] = 'X'
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')


def check_win(sign):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], sign)
        check_line(field[0][n], field[1][n], field[2][n], sign)
    check_line(field[0][0], field[1][1], field[2][2], sign)
    check_line(field[2][0], field[1][1], field[0][2], sign)


def check_line(a1, a2, a3, sign):
    if a1['text'] == sign and a2['text'] == sign and a3['text'] == sign:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False


def can_win(a1, a2, a3, sign):
    res = False
    if a1['text'] == sign and a2['text'] == sign and a3['text'] == start_text:
        a3['text'] = 'O'
        res = True
    if a1['text'] == sign and a2['text'] == ' ' and a3['text'] == sign:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == sign and a3['text'] == sign:
        a1['text'] = 'O'
        res = True
    return res


def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return

    while True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if field[row][column]['text'] == start_text:
            field[row][column]['text'] = 'O'
            break


for row in range(3):
    line = []
    for column in range(3):
        button = Button(root, text=' ', width=6, height=3,
                        font=('Verdana', 20, 'bold'),
                        background=background,
                        command=lambda row=row, column=column: click(row, column))
        button.grid(row=row, column=column, sticky='nsew')
        line.append(button)

    field.append(line)

new_button = Button(root, text='New Game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

root.mainloop()
