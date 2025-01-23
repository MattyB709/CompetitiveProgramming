n = int(input())
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n /= 2
        n = int(n)
    else:
        n = n * 3 + 1
    
print(n)