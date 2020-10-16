# незнаю что это значит и как сделать
# я просто скопировал код с Tproger
# 19.04.2020
from os import listdir
from os.path import isfile, join
files = [f for f in listdir('/home') if isfile(join('/home', f))]
print(files)