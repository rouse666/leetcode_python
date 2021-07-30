def bubblesort(list):
    n = len(list)
    for k in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j + 1]:
                list[j + 1], list[j] = list[j], list[j + 1]
        print(list)


alist = [4, 5, 12, 3, 8, 9]
bubblesort(alist)
print(alist)
