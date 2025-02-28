n, k = map(int, input().split())
mins = list(map(int, input().split()))

sum = 0
temp = 0
for num in mins:
    temp += num
    temp -= k
    temp = 0 if temp < 0 else temp
    sum += 1
while temp > 0:
    sum += 1
    temp -= k
print(sum)
    