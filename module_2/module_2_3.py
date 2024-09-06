my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = len(my_list)
while i > 0:
    n = my_list.pop(0)
    i = i - 1
    if n > 0:
        print(n)
    elif n < 0:
        break