n = input()
apples = list(map(int, input().split()))


min = [sum(apples)]
def recurse(current_apple:int, bucket1, bucket2):
    if current_apple == len(apples):
        diff = abs(bucket1 - bucket2)
        if diff < min[0]:
            min[0] = diff
    else:
        bucket1 += apples[current_apple]
        recurse(current_apple + 1, bucket1, bucket2)

        bucket1 -= apples[current_apple]
        bucket2 += apples[current_apple]
        recurse(current_apple + 1, bucket1, bucket2)
        bucket2-= apples[current_apple]
recurse(0, 0, 0)
print(min[0])
    

