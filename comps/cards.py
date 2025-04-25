class FenwickTree:
    def __init__(self, n):
        # Initialize a Fenwick Tree with n elements (1-indexed)
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        # Update index i (1-indexed) with delta.
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
    
    def query(self, i):
        # Return the prefix sum from index 1 to i (inclusive)
        result = 0
        while i:
            result += self.tree[i]
            i -= i & -i
        return result

# Read input
n = int(input())
cards = list(map(int, input().split()))

bit_count = FenwickTree(n)
bit_sum = FenwickTree(n)

score = 0

for c in cards:
    count_greater = bit_count.query(n) - bit_count.query(c)
    sum_greater = bit_sum.query(n) - bit_sum.query(c)
    
    score += count_greater * c + sum_greater
    
    bit_count.update(c, 1)
    bit_sum.update(c, c)

print(score)
