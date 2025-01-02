# compute module for all calculation functions
from fractions import Fraction

# check if an integer is divisible by a given integer
def is_divisible(divisor: int, dividend: int):
    # error handling for non-integers?
    return dividend % divisor == 0


# convert decimal to fraction
def to_fraction(decimal):
    ratio = Fraction(decimal).limit_denominator().as_integer_ratio()
    
    ratio_as_string = f'{ratio[0]}/{ratio[1]}'
    
    return ratio_as_string


# compute p-adic valuation on an integer
#   the p-adic valuation of an integer is highest power of the prime that 
#   divides the integer
def valuation(prime: int, integer: int):
    # initialize valuation
    valuation = 0

    # check if integer is zero
    if integer == 0:
        return float('inf')
    
    # check divisibility
    remainder = is_divisible(prime, integer)

    while remainder:
        # increment valuation every time integer is divisible by prime
        valuation += 1
        integer = integer / prime
        remainder = is_divisible(prime, integer)
    
    return valuation


# compute the p-adic valuation of a rational number
#   the p-adic valuation of a rational number is the difference between
#   the valuations on the numerator and the denominator
def valuation_rational(prime: int, rational):    
    # check if rational is zero
    if rational == 0:
        return float('inf')

    # convert float to ratio of integers a/b
    # see https://docs.python.org/3/library/fractions.html
    # ratio = Fraction(rational).limit_denominator().as_integer_ratio()
    ratio = Fraction(eval(str(rational))).limit_denominator().as_integer_ratio()
    
    # compute valuation of numerator 
    a = valuation(prime, ratio[0])

    # compute valuation of denominator
    b = valuation(prime,ratio[1])

    # compute difference
    # no need to create a pointer for this if returning it?
    val = a - b

    return val


# compute p-adic absolute value of a rational number
#   the p-adic absolute value of a number is the reciprocal of the prime number
#   raised to its valuation on that number
def p_adic_abs(prime: int, rational):
    
    # compute valuation
    val = valuation_rational(prime, rational)

    # check if valuation is infinite (i.e. rational is zero)
    if val == float('inf'):
        return {
            'valuation': val,
            'float': 0,
            'fraction': 0
        }

    # compute p-adic norm
    abs = 1/((prime)**(val))

    # refactor as class method?
    if val <= 0:
        abs = int(abs)
        return {
            'valuation': val,
            'float': abs,
            'fraction': abs
        }
    else:    
        return { 
            'valuation': val,
            'float': round(abs,12),
            'fraction': to_fraction(abs)
        }