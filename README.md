# p-adic Absolute Value

The module `p_adic_abs` contains functions to calculate the p-adic absolute-value of a rational number.

The function `p_adic_abs` takes a prime $p$ and a rational number $x$ as its arguments and returns the 
p-adic absolute value $|x|_p$ as a float.

The float can be converted to an integer ratio with the `fractions` package.

Example:

    import p_adic_abs
    p = p_adic_abs.p_adic_abs(5, 200)
    0.008

    from fractions import Fraction
    Fraction(p).limit_denominator().as_integer_ratio()
    (1, 125)
