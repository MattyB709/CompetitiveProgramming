import sys
n, m = map(int, input().split())
matrix = [list(map(int, line.split())) for line in sys.stdin]

def recurse(i, j, reward, max_reward):
    if j == m:
        return 0
    # print(i)
    reward += matrix[i][j]
    max_reward = reward if reward > max_reward else max_reward
    # print("i, j, :", i, j)
    # print(reward)
    # print(max_reward)
    # print()
    if i == 0:
        reward_up = recurse(n-1, j+1, reward, max_reward)
    else: 
        reward_up = recurse(i-1, j+1, reward, max_reward)
    # print("reward up: ", reward_up, i, j)
    max_reward = reward_up if reward_up > max_reward else max_reward
    if i == n-1:
        reward_down = recurse(0, j+1, reward, max_reward)
    else:
        reward_down = recurse(i+1, j+1, reward, max_reward)
    # print("reward_down: ",reward_down)
    max_reward = reward_down if reward_down > max_reward else max_reward
    return max_reward

max_reward = 0
# max_reward = recurse(0, 0, 0, max_reward)
for i in range(n):
    reward = recurse(i, 0, 0, max_reward)
    max_reward = reward if reward > max_reward else max_reward
print(max_reward)