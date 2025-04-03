def solve():
    import sys
    import bisect

    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    card_w = int(next(it))
    card_h = int(next(it))
    
    envelopes = []
    # Read envelopes and filter those that can contain the card.
    for i in range(n):
        w = int(next(it))
        h = int(next(it))
        if w > card_w and h > card_h:
            # store envelope with (width, height, original_index)
            envelopes.append((w, h, i+1))
            
    # If no envelope can even contain the card, print 0.
    if not envelopes:
        sys.stdout.write("0")
        return

    # Sort envelopes by width asc; if width equal, sort by height desc.
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    m = len(envelopes)
    # dp will hold the smallest ending height for each length of chain found so far.
    dp = []
    # dp_index stores the indices (in envelopes list) that end the chain of length len+1.
    dp_index = []
    # prev will help us reconstruct the chain.
    prev = [-1] * m

    for i in range(m):
        _, h, _ = envelopes[i]
        # Find position where h could be inserted (strictly increasing, so we want dp[j] < h)
        pos = bisect.bisect_left(dp, h)
        if pos == len(dp):
            dp.append(h)
            dp_index.append(i)
        else:
            dp[pos] = h
            dp_index[pos] = i
        if pos > 0:
            prev[i] = dp_index[pos-1]

    # Reconstruct the chain by backtracking from the last element of the best chain.
    chain = []
    idx = dp_index[-1]
    while idx != -1:
        chain.append(envelopes[idx][2])  # original envelope index
        idx = prev[idx]
    chain.reverse()

    # Output the result.
    output = []
    output.append(str(len(chain)))
    output.append(" ".join(map(str, chain)))
    sys.stdout.write("\n".join(output))
    
solve()
