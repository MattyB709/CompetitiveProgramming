n, k = map(int, input().split())
array = list(map(int, input().split()))

def check_num(array, num, k):
    j = 0
    for i in range(k):
        sub_sum = 0
        while True:
            if j == len(array):
                return True
            if sub_sum + array[j] <= num:
                sub_sum += array[j]
                j += 1
            else:
                break
    return False

low = 0
high = sum(array)
while low < high:
    mid = low + (high - low) // 2
    if check_num(array, mid, k):
        high = mid
    else:
        low = mid + 1
print(low)


