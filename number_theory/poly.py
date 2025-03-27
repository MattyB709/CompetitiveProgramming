import math
total = 0
for i in range(1000):
    sum = i ** 5 - 2 * i **4 + 2 * i +1
    if sum % 10 == 0:   
        total+= 1
        print("i: ",i)
        print("sum: ",sum % 10)
print(total)