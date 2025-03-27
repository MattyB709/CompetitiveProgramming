def precompute_f_table(mod):
    """
    Precompute a table for f(x) = product of numbers 1..x that are
    coprime to 10 modulo mod. 
    f(i*mod + j) is equivalent to f(j) (mod mod), so we can just compute this up to mod.
    """
    table = [1] * (mod)
    for x in range(1, mod):
        if x % 2 != 0 and x % 5 != 0:
            table[x] = (table[x - 1] * x) % mod
        else:
            table[x] = table[x - 1]
    return table

def f(x, mod, table):
    """
    Returns f(x) = product of numbers 1..x that are coprime to 10, modulo mod.
    The modulo here is because f(x mod mod) is equal to f(x)
    """
    return table[x % mod]

def generate_hamming(n):
    """
    Generate all numbers of the form 2^a * 5^b that are <= n (aka hamming numbers)
    """
    hs = set()
    a = 1
    while a <= n:
        b = a
        while b <= n:
            hs.add(b)
            b *= 5
        a *= 2
    return hs

def count_factor(n, p):
    """
    Count the exponent of the prime p in n, which for us will just be 2 and 5
    """
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count

def last_nonzero_digits(n, k):
    """
    Compute the last k nonzero digits of n!.
    
    The method works by writing:
       n! = 2^(e2) * 5^(e5) * R,
    where R is not divisible by 2 or 5.
    The last nonzero digits come from R multiplied by the leftover 2's
    (i.e. 2^(e2-e5)), all computed modulo 10^k (5 for our case)
    
    Here, we compute R indirectly by grouping the contributions from
    numbers that are coprime to 10. In fact, every number i in 1..n can be
    uniquely written as (2^a * 5^b)*r with r coprime to 10. let d = 2^a * 5^b, then
    the product of all r's is equal to the product of f(n // d) mod 10^k 
          f(n // d)   mod 10^k,
    for all possible d that are less than or equal to n, or (10^16)!
    Here, f(x) is the product of all numbers less than or equal to x that are coprime to 2 and 5
    
    We then multiply by leftover factors of 2
    """
    mod = 10 ** k

    # precompute f(x) for x up to mod
    table = precompute_f_table(mod)

    # compute the product over all numbers d = 2^a * 5^b <= n:
    hamming_numbers = generate_hamming(n)
    prod = 1
    # efficient calculation of R
    for d in hamming_numbers:
        prod = (prod * f(n // d, mod, table)) % mod

    # Count factors in n!:
    total_twos = count_factor(n, 2)
    total_fives = count_factor(n, 5)
    print("trailing zeros: ", total_fives)
    extra_twos = total_twos - total_fives

    # Multiply by the extra powers of 2:
    result = (prod * pow(2, extra_twos, mod)) % mod

    return result

n = 10**16
print(f"Last 5 nonzero digits of {n}! = {last_nonzero_digits(n,5)}")
