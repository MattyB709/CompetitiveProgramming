import sys
n = input()

lis = []
for line in sys.stdin:
    a, b = map(int, line.split())
    ops = 0
    
    while a > 0 and b > 0:
        if b > a:
            q = b // a
            ops += q
            b = b % a
        else:
            q = a//b
            ops += q
            a = a%b

    print(ops)