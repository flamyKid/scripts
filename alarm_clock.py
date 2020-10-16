import time
import datetime

year = int(input('Год: '))
month = int(input('Месяц: '))
day = int(input('День: '))
hour = int(input('Час: '))
minutes = int(input('Минуты: '))

while True:
    now_year = datetime.datetime.now().year
    now_month = datetime.datetime.now().month
    now_day = datetime.datetime.now().day
    now_hour = datetime.datetime.now().hour
    now_minutes = datetime.datetime.now().minute

    if year == now_year and month == now_month \
            and day == now_day and hour == now_hour \
            and minutes == now_minutes:
        print('Время!')
        break
