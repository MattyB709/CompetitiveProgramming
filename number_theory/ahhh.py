from math import factorial

def brute_force_last_nonzero(n, k=5):
    """
    Compute the last k nonzero digits of n! exactly.
    This method works for small n by computing n! exactly,
    then removing the trailing zeros, and finally extracting
    the last k digits.
    
    Parameters:
      n (int): The input for which to compute n!
      k (int): Number of nonzero digits to return (default 5)
    
    Returns:
      A string of exactly k digits (with leading zeros if needed).
    """
    # Compute n! exactly using Python's built-in factorial (which uses arbitrary precision)
    f = factorial(n)
    
    # Remove trailing zeros (i.e. divide by 10 until the last digit is nonzero)
    while f % 10 == 0:
        f //= 10
    
    # Convert the resulting number to a string, then take the last k digits.
    return f % 10**5

# Test the algorithm for small values of n:
for n in [10**6]:
    print(f"{n}! last 5 nonzero digits: {brute_force_last_nonzero(n)}")
