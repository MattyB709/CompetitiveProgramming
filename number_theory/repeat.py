import math
found_square = False
num = 1
while not found_square:
    rep_string = str(num) * 2
    rep_int = int(rep_string)
    if math.sqrt(rep_int).is_integer():
        found_square=True
    num += 1
print(num)