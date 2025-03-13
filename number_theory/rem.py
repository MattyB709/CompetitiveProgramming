sum = 0
n = 0
while(n < 26):
    n += 1
    sum += n*n
    print(sum)
    if sum % n == 0:
        print(n)