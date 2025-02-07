import math
n = input()
nums = list(map(int, input().split()))
# for this problem it shouldn't be necessary to do 1 indexing
prefix_sums = [0] * (len(nums))
sum = 0
all_zeroes = True
for i, num in enumerate(nums):
    prefix_sums[i] = sum + num
    sum += num
    if not num == 0:
        all_zeroes = False

if not prefix_sums[-1] % 3 == 0:
    print(0)
else:
    # if it is all_zeroes, it's just a combination problem 
    if all_zeroes:
        print(math.comb(len(prefix_sums)-1, 2))
    else:
        sub_sum = prefix_sums[-1] / 3
        # Use faster method for longer sequences
        if len(prefix_sums) > 100:
            sum1 = 0
            sum2 = 0
            for num in prefix_sums:     
                if (num == sub_sum):
                    sum1 += 1
                elif num == 2 * sub_sum:
                    sum2 += 1
            print(sum1 * sum2)
        # Use slower method on short sequences
        else:
            index = 0
            count = 0 
            for r1 in range(len(prefix_sums) - 2):
                for r2 in range(r1 + 1, len(prefix_sums) - 1):
                    if (prefix_sums[r1] == sub_sum and prefix_sums[r2] == sub_sum * 2):
                        count += 1
            print(count)