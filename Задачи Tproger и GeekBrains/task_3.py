# 16.04.2020
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

item = list(d.items())
item.sort(key=lambda x: x[1])

print(item)
