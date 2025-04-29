import matplotlib.pyplot as plt
import math

# Problem 3
# Function for creating the lookup tables of Legendre symbols for any prime p, computes linearly
def find_legendre_symbols(p):
    # initialize an array of size p, all filled with -1
    legendre_symbols = [-1] * p
    for i in range(1, p): #1..p-1
        legendre_symbols[(i*i) % p] = 1 # set all squares to 1

    legendre_symbols[0] = 0 
    return legendre_symbols

# Problem 2
# Direct computation of a_p using the definition of f
def slow_ap(p, a, b):
    a_p = 0
    # get the lookup table of legendre symbols
    lookup_table = find_legendre_symbols(p)
    for x in range(p):
        # calculate f(x) directly modulo p, then index into the lookup table to find its
        # Legendre symbol
        val = lookup_table[f(x, a, b) % p]
        a_p+= val
    return a_p

# Implementation of problem 4
# These are the finite difference functions, i.e f(x), del f(x), del^2 f(x)
def f(x, a, b):
    return x**3 + a * x + b

def del_f(x, a):
    return 3*x**2 + 3*x + a + 1

def del_2_f(x):
    return 6*x+6

# Problem 5
# computation of a_p using finite difference formula, 
def compute_ap(p, a, b):
    lookup_table = find_legendre_symbols(p)
    # calculate the initial values for each function
    fx = f(0, a, b) % p
    df = del_f(0, a) % p
    d2f = del_2_f(0) % p
    d3f = 6 % p
    # a_p will be a running sum of the legendre symbols
    ap = lookup_table[fx]
    for x in range(1, p): # compute every x in F_p except for 0 using the finite difference formulas
        fx = fx + df
        # subtract by p as given in the implementation note, only if x+y >= p
        fx = fx - p if fx >= p else fx

        df = df + d2f
        df = df - p if df >= p else df

        d2f = d3f + d2f
        d2f = d2f - p if d2f >= p else d2f

        ap += lookup_table[fx]

    return ap


# Sieve of Eratosthenes up to M (M chosen to result in >5000 primes)
def get_primes():
    M = 60000
    sieve = [True] * (M + 1)
    sieve[0] = sieve[1] = False

    # isqrt(M) returns the biggest integer n such that n^2 <= M. We only need to check up to the sqrt  
    for p in range(2, int(math.isqrt(M)) + 1):
        if sieve[p]:
            
            # cross out all multiples of the current number
            for multiple in range(p*p, M+1, p):
                sieve[multiple] = False

    # extract all numbers in the sieve that are left with true, using list comprehension to put them
    # into one big list
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    # return the first 5000
    return primes[:5000]

# Problem 6
# Code used to create histograms problem 6 for each set of parameters, for ease of use this
# code was run in a jupyter notebook, but placed here
def plot_tp():
    # list of 5000 primes
    primes = get_primes()
    params = [(1,1),(0,1),(2,1),(-3,2)]
    for a, b in params:
        tp = []
        for i in range(len(primes)):
            # for every prime, compute a_p, then get a list of t_p to plot on a histogram
            p = primes[i]
            ap = compute_ap(p, a, b)
            tp.append(ap /(2 * math.sqrt(p)))
        
        # Use matplotlib's histogram functionality
        plt.figure()
        plt.hist(tp, bins=70)
        plt.title(f"Histogram for (a,b) = ({a}, {b})")
        plt.ylabel("frequency")
        plt.xlabel("t_p")
        plt.show()
    
# Problem 7 (i)
def problem_7():
    # p equiv 1, -1 mod 3
    primes = get_primes()
    prime_one = []
    prime_negative_one = []

    for p in primes:
        if p % 3 == 1:
            prime_one.append(p)
        # -1 = 2 (mod 3)
        elif p % 3 == 2:
            prime_negative_one.append(p)

    # evaluate tp for primes in each list, then output their graphs
    tp = []
    for i in range(len(prime_one)):
        p = prime_one[i]
        ap = compute_ap(p, 0, 1)
        tp.append(ap /(2 * math.sqrt(p)))
    plt.figure()
    plt.hist(tp, bins=70)
    plt.title(f"Histogram for (a,b) = ({0}, {1}), p = 1 (mod 3)")
    plt.ylabel("frequency")
    plt.xlabel("t_p")
    plt.show()

    tp = []
    for i in range(len(prime_negative_one)):
        p = prime_negative_one[i]
        ap = compute_ap(p, 0, 1)
        tp.append(ap /(2 * math.sqrt(p)))
    plt.figure()
    plt.hist(tp, bins=70)
    plt.title(f"Histogram for (a,b) = ({0}, {1}), p = -1 (mod 3)")
    plt.ylabel("frequency")
    plt.xlabel("t_p")
    plt.show()
