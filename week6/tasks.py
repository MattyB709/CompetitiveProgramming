import heapq
n = int(input())
heap = []
for _ in range(n):
    a, d = map(int, input().split())
    heapq.heappush(heap, (a, d))
time = 0
score = 0
while not len(heap) == 0:
    t, deadline = heapq.heappop(heap)
    time += t
    score += deadline - time
print(score)