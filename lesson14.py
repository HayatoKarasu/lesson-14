my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def tmp(x):
    if x <= 0:
        return
    tmp(x - 1)
    print(x, end = " ")


tmp(16)
print("Конец списка")
