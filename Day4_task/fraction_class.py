# Task 08: Dunder Methods — Custom Fraction Class
# Implements a Fraction class with arithmetic and comparison dunder methods.

import math
from functools import total_ordering


@total_ordering  
class Fraction:
    """A class representing a mathematical fraction with full dunder method support."""

    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        # Simplify on creation using GCD
        common = math.gcd(abs(numerator), abs(denominator))
        self.numerator   = numerator   // common
        self.denominator = denominator // common

    def __str__(self) -> str:
        """Displays the fraction as 'numerator/denominator'."""
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other: "Fraction") -> "Fraction":
        """Adds two fractions: a/b + c/d = (ad + bc) / bd, then simplifies."""
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)   # simplification happens in __init__

    def __eq__(self, other: "Fraction") -> bool:
        """Returns True if two fractions are equal after simplification."""
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other: "Fraction") -> bool:
        """Returns True if this fraction is less than the other (a/b < c/d)."""
        return self.numerator * other.denominator < other.numerator * self.denominator


#  Test with 3 pairs of fractions 
if __name__ == "__main__":
    f1 = Fraction(1, 2)  
    f2 = Fraction(1, 3)  
    f3 = Fraction(2, 4)
    f4 = Fraction(3, 4)  
    f5 = Fraction(2, 3)  
    f6 = Fraction(5, 6)  

    print(" Pair 1: 1/2 and 1/3 ")
    print(f"  {f1} + {f2}  = {f1 + f2}")
    print(f"  {f1} == {f2} = {f1 == f2}")
    print(f"  {f1} <  {f2} = {f1 < f2}")

    print("\n Pair 2: 1/2 and 2/4 (equal after simplification) ")
    print(f"  {f1} == {f3} = {f1 == f3}")   
    print(f"  {f1} + {f3}  = {f1 + f3}")

    print("\n Pair 3: 2/3 and 5/6 ")
    print(f"  {f5} + {f6}  = {f5 + f6}")
    print(f"  {f5} <  {f6} = {f5 < f6}")
    print(f"  {f4} >  {f2} = {f4 > f2}")   # > works via @total_ordering — no extra code needed!


# EXPLORE: @functools.total_ordering 
# With only __eq__ and __lt__ defined, @total_ordering automatically generates
# __le__, __gt__, and __ge__ for you. Without it, you'd need to manually write
# all 4 comparison methods. It reduces boilerplate while keeping the class complete.