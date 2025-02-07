nums = list(map(int, input().split()))
start = nums[0]
end = nums[1]
       
count = 0
while not end == start:
    if end < start:
        end+=1
        count += 1
    else:
        if end % 2 == 0:
            end /= 2
            count += 1
        else:
            end += 1
            count += 1
print(count)