def last_five_nonzero_digits(n):
    # Convert n to base 5
    base5_representation = convert_to_base5(n)
    
    # Initialize lookup tables
    # These would be pre-computed tables for the patterns of last 5 non-zero digits
    # based on position and digit in base-5 representation
    initialize_lookup_tables()
    
    # Calculate the last 5 non-zero digits recursively
    result = recursive_calculate(base5_representation, 5)
    
    return result

def recursive_calculate(base5_digits, digits_count):
    # Base case
    if len(base5_digits) == 0:
        return 1
    
    # Decompose n = 5a + b where b is the last digit in base 5
    b = int(base5_digits[-1])
    a_base5 = base5_digits[:-1]
    
    # Recursively calculate the contribution of a!
    a_contribution = recursive_calculate(a_base5, digits_count)
    
    # Calculate 2^a mod 10^digits_count
    a_value = convert_from_base5(a_base5)
    power_of_2 = pow(2, a_value, 10**digits_count)
    
    # Calculate the contribution of b!
    b_contribution = factorial_mod(b, 10**digits_count)
    
    # Combine using the formula: L(n!) = Last Digits of [2^a × L(a!) × L(b!)]
    result = (power_of_2 * a_contribution * b_contribution) % (10**digits_count)
    
    # Remove trailing zeros
    while result % 10 == 0 and result > 0:
        result //= 10
    
    return result
