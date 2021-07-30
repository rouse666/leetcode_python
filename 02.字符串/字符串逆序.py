s = input()
space = ''
for i in range(len(s), 0, -1):
    space += s[i - 1]
print(space)
