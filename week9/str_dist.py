n = int(input())
lines = [''] * n
fs = 1
for i in range(n):
    lines[i] = input()
    if lines[i] == 'f': 
        fs += 1
array = [[''] * fs for _ in range(n)]
array_nums = [[0] * fs for _ in range(n - 1)]
array_nums.append([1] * fs)
indent = 0
for i, line in enumerate(lines):
    array[i][indent] = line
    if line == 'f':
        indent += 1
print(array)
print(indent)
for i in reversed(range(n - 1)):
    if array[i][indent] == '':
        indent -= 1
    if array[i-1][indent - 1] == 'f':
        print("hello")
        indent -= 1
        continue
    for k in range(indent + 1):
        sum = 0
        for j in range(indent + 1):
            sum += array_nums[i+1][j]
        array_nums[i][k] = sum
    
print(array_nums)