from time import time

ns = [100,200,500,1000]

for n in ns:
    mat = [[i] * n for i in range(n)]
    mat2 = [[i] * n for i in range(n)]
    mat3 = [[i] * n for i in range(n)]

    t = time()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat3[i][j] += mat[i][k] * mat2[k][j]

    print(time() - t)
    t = time()
    for i in range(n):
        for k in range(n):
            for j in range(n):
                mat3[i][j] += mat[i][k] * mat2[k][j]
    print(time() - t)
