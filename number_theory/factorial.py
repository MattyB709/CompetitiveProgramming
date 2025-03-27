def trailing_zeros_in_factorial_of_10_to_n(n):
    """
    Calculate the number of trailing zeros in (10^n)!
    
    Args:
        n (int): The exponent of 10
        
    Returns:
        int: Number of trailing zeros
    """
    if n < 0:
        return "Please enter a non-negative integer"
    
    num = 10 ** 16
    count = 0
    power = 5
    
    # Sum the number of factors of 5
    while power <= num:
        count += num // power
        power *= 5
        
    return count

# Test the function
def main():
    print(trailing_zeros_in_factorial_of_10_to_n(16))

if __name__ == "__main__":
    main()