import sys
n, m = map(int, input().split())
matrix = [list(map(int, line.split())) for line in sys.stdin]

max_power = 0
# print(*matrix)
i = 0
current_power = 0
found_hole = False
hole_index = 0
while i < n:
    
    num_zeros = 0
    for j in range(m):
        if matrix[i][j] == 0 and num_zeros == 0:
            num_zeros += 1
        elif matrix[i][j] == 0 and num_zeros > 0:
            num_zeros += 1
            break
    
    if num_zeros == 1:
        if found_hole:
            i = hole_index
            found_hole = False
            current_power = 0
        else:
            found_hole = True
            hole_index = i
            current_power += 1
            max_power = current_power if current_power > max_power else max_power
    elif num_zeros == 0:
        current_power += 1
        max_power = current_power if current_power > max_power else max_power
    else: 
        current_power = 0
    i+=1

j = 0
current_power = 0
found_hole = False
hole_index = 0
while j < m:
    
    num_zeros = 0
    for i in range(n):
        if matrix[i][j] == 0 and num_zeros == 0:
            num_zeros += 1
        elif matrix[i][j] == 0 and num_zeros > 0:
            num_zeros += 1
            break
    
    if num_zeros == 1:
        if found_hole:
            j = hole_index
            found_hole = False
            current_power = 0
        else:
            found_hole = True
            hole_index = j
            current_power += 1
            max_power = current_power if current_power > max_power else max_power
    elif num_zeros == 0:
        current_power += 1
        max_power = current_power if current_power > max_power else max_power
    else: 
        current_power = 0
    j+=1
print(max_power)