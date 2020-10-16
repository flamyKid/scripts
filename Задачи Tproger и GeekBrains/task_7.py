# 19.04.2020
# тож не придумал как реализовать
def pascal_trnlg(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]


pascal_trnlg(6)