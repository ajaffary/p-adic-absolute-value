import math
from fractions import Fraction

# model module to store user input data?
# prime = default
# rational = default

# view to communicate with user
# get_prime
# get_rational

# compute contains all calculation functions

def is_divisible(divisor, dividend):
    # error handling for non-integers?
    # refactor into compute module?
    return dividend % divisor == 0

# this is INCORRECT and will not produce the correct valuation
def valuation(prime, number):
    # refactor into compute module?
    remainder = is_divisible(prime, number)
    if remainder:
        valuation = int(math.log(number, prime))
    else: 
        valuation = 0
    return valuation

def p_adic_abs(prime, number):
    # refactor into compute module?
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


# controller communicates between view and model
# import model, view
# model.prime = view.get_prime()
# model.rational = view.get_rational()
# view.present_output(model.prime, model.rational)