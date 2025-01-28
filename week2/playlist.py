n = input()
songs = input().split()
l = 0
r = 1
freqs = {}
max = 0
for l, num in enumerate(songs):
    if songs[l] not in freqs:
        freqs[songs[l]] = 1
    while (r < len(songs)):
        # first time encountering it
        if songs[r] not in freqs:
            freqs[songs[r]] = 1
            r+=1
        # not first time encountering element, but current frequency is 0    
        elif freqs[songs[r]] == 0:
            freqs[songs[r]] = 1
            r+=1
        # this element is in our current stream, now we need to move l forward
        elif freqs[songs[r]] >= 1:
            break
        else:
            #shouldn't happen, debugging purposes
            print(freqs[songs[r]])
    max = r - l if r - l > max else max
    freqs[songs[l]]-= 1
    l+=1
print(max)
