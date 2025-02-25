num_queries = int(input())


def check_count(time, hours):
    over_sum = 0
    under_sum = 0
    for hour in hours:
        if hour < time:
            under_sum += (time - hour) // 2
        else:
            over_sum += hour - time
    # print("over sum: ", over_sum)
    # print("under sum: ", under_sum)
    return over_sum <= under_sum 

for _ in range(num_queries):
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    hours = [0] * n
    for task in tasks: 
        hours[task - 1] += 1
    l = 1
    r = max(hours) + m * 2 
    # stop when we have an array of size 1
    while l < r:
        time = (r + l) // 2
        # print("l: ", l)
        # print("r: ", r)
        # print("time: ", time)
        can_complete = check_count(time, hours)  
        if can_complete:
            # print("can complete")
            r = time
        else: 
            # print("can't complete")
            l = time + 1
    print(int(l))

     


