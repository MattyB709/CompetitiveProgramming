
num1, num2 = map(int, input().split())
def euclid(n,m):
    if n == 0:
        return m
    elif m == 0:
        return n
    else:
        if n > m:
            return euclid(n % m, m)
        else:
            return euclid(n, m % n)

print(euclid(num1, num2))