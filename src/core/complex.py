"""
In math, imaginary unit or complex unit is a complex number, Denoted-
by letter 'i'. Where i=√(-1) and i^2 is defined as -1. Using this concept,-
we can get a number whose square is negative.

The simple application of complex number is quadratic equation whose solution-
is not exist on real domain (their discriminant is less than zero)-
Example:
x^2 + 1 = 0
x = ±√(-1) = ±i
"""
import typing


def imag_pow_to(n) -> typing.Union[str, int]:
    p = n%2
    k = (n - p)/2
    return str(int((-1)**k)) + ('i' if p else '')
