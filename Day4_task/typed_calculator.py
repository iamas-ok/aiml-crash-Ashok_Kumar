# Task 04: Type-Hinted Calculator Module
# A fully type-hinted calculator with basic operations, power, modulo, and safe divide.

from typing import Optional


def add(a: float, b: float) -> float:
    # Adds two numbers and returns the result
  
    return a + b


def subtract(a: float, b: float) -> float:
    # Subtracts b from a and returns the result 
    return a - b


def multiply(a: float, b: float) -> float:
    # Multiplies two numbers and returns the result
    return a * b


def divide(a: float, b: float) -> Optional[float]:
#    Divides a by  b and returns the result. Returns None if b is zero instead of raising an error.
    if b == 0:
        return None
    return a / b


def power(base: float, exp: float) -> float:
    # Raises base to the power of exp and returns the result
    return base ** exp


def modulo(a: int, b: int) -> Optional[int]:
#     Returns the remainder of a divided by b. Returns None if b is zero to handle division by zero safely.
    if b == 0:
        return None
    return a % b



if __name__ == "__main__":
    print("Addition       :", add(10, 5))
    print("Subtraction    :", subtract(10, 5))
    print("Multiplication :", multiply(10, 5))
    print("Division       :", divide(10, 5))
    print("Division by 0  :", divide(10, 0))  
    print("Power          :", power(2, 8))
    print("Modulo         :", modulo(17, 5))
    print("Modulo by 0    :", modulo(17, 0))    


#EXPLORE 
# Optional[float] from the typing module means the function can return
# either a float OR None. It is shorthand for Union[float, None].
# This is safer than raising an exception because the caller can check
# "if result is None" instead of wrapping every call in a try/except.