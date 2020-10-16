# 19.04.2020
def file_extension(filen):
    filename = filen.split('.')
    if len(filename) < 2:
        raise ValueError
    first, *middle, last = filename
    if not last or not first and not middle:
        raise ValueError
    return filename[-1]

file_extension('abc.py')
file_extension('dhfjfl.d')
file_extension('.abc')