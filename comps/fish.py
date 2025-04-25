n = int(input())
top =       "o-----------------------o"
fish_rows = "|        <><            |"
rows =      "|                       |"
print(top)
for _ in range(n):
    print(fish_rows)
for _ in range(13 - n):
    print(rows)
print(top)