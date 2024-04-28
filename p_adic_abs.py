import math
from fractions import Fraction

def is_divisible(divisor, dividend):
    # error handling for non-integers
    return dividend % divisor == 0

def valuation(prime, number):
    remainder = is_divisible(prime, number)
    if remainder:
        valuation = int(math.log(number, prime))
    else: 
        valuation = 0
    return valuation

def p_adic_abs(prime, number):
    # convert float to fraction a/b
    # use https://docs.python.org/3/library/fractions.html
    # use rational = Fraction(number).limit_denominator().as_integer_ratio()
    rational = Fraction(number).limit_denominator().as_integer_ratio()
    
    # check if a = rational[0] is divisible by p
    # compute valuation(a)
    a = valuation(prime, rational[0])
    # check if b = rational[1] is divisible by p
    # compute valuation(b)
    b = valuation(prime,rational[1])

    val = a - b

    abs = 1/((prime)**(val))

    # question:  return as float or fraction?
    return abs

