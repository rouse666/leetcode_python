A, B = map(int, input().split())
T = 1
for i in range(2, min(A, B) + 1):  # 只需遍历到最小一个数
    while A % i == 0 and B % i == 0:  # 逐一找到公共除数
        T = T * i  # 找到公共除数就累乘
        A = A // i
        B = B // i
print(A * B * T)
