# Exercise 1a: Fibonacci Recursive (★✩✩✩✩)
# Write function fib_rec(n) that recursively computes Fibonacci numbers based on the
# following definition: fib(n) = 1 if n=1||n=2 , sonst = fib(n-1) + fib(n-2)
# Example
# For example, check the implementation with the following value progression:
# Input 1 2 3 4 5 6 7 8 fib(n) 1 1 2 3 5 8 13 21
def fib(n):
    if n <= 0:
        raise ValueError('n must be >=1')
    # recursive termination
    if n == 1 or n == 2:
        return 1
    # recursive descent
    return fib(n - 1) + fib(n - 2)


# OneLiner
fib_short = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)


# Exercise 1b: Fibonacci Iterative (★★✩✩✩)
# The recursive calculation of Fibonacci numbers is not efficient,
# and the running time increases enormously from about the fortieth or fiftieth Fibonacci number. Write an iterative
# version for the calculation.


# Exercise 2a: Count Digits (★★✩✩✩)
# Write recursive function count_digits(value) that finds the number of digits in a positive natural number.
# We already discussed how to extract digits in the previous chapter in section 2.1.


# Exercise 2b: Cross Sum (★★✩✩✩) Calculate the sum of the digits of a number recursively. Write recursive function
# calc_sum_of_digits(value) for this purpose.


# Exercise 3a: GCD Recursive (★✩✩✩✩)
# Write function gcd(a, b) that computes the greatest common divisor (GCD)1. GCD can be expressed mathematically
# recursively as follows for two natural numbers a and b: gcd(a,b) = a, if b=0 ; = gcd(b,a%b if b!=0

def gcd(a, b):
    # recursive termination
    if b == 0:
        return a
    # recursive descent
    return gcd(b, a % b)

# Exercise 3b: GCD Iterative (★★✩✩✩)
# create an iterative version for the GCD calculation.


# Exercise 3c: LCM (★✩✩✩✩)
# Write function lcm(a, b) that computes the least common multiplier (LCM). For two natural numbers a and b,
# you can calculate this based on the GCD using the following formula:


# Exercise 4: Reverse String (★★✩✩✩)
# Write recursive function reverse_string(text) that flips the letters of the text passed in.


# Exercise 5: List Sum (★★✩✩✩)
# Write function sum_rec(values) that recursively computes the sum of the values of the
# given list. No call to the built-in functionality sum() is allowed.


# Exercise 6: List Min (★★✩✩✩)
# Write function min_rec(values) that uses recursion to find the minimum value of the passed list.
# For an empty list, the value sys.maxsize should be returned. In the implementation, no call to the built-in
# functionality min() is allowed.


# Exercise 7: Conversions (★★✩✩✩) Exercise 7a: Binary (★★✩✩✩)
# Write function to_binary(n) that recursively converts the given positive integer into a textual binary representation.
# No call to int(x, base) may be used.


# Exercise 7b: Octal and Hexadecimal Numbers (★★✩✩✩)
# Write conversions to octal and hexadecimal numbers by implementing the corresponding functions to_octal(n) and to_
# hex(n). Again, no call to int(x, base)
# may be used.


# Exercise 8a: Power of Two (★★✩✩✩)
# Write recursive function is_power_of_2(n) that evaluates the given positive integer to see if it is a power of two.


# Exercise 8b: Exponentiation Recursive (★★✩✩✩) Write recursive function power_of(value, exponent) that exponentiates
# the given positive integer with the positive number specified as second parameter. For example, the call power_of(
# 4, 2) should return the square of 4, so compute 42 = 16. You may not use the built-in functionality pow() or the
# operator **.


# Exercise 8c: Exponentiation Iterative (★★✩✩✩)
# Write an iterative version of this exponentiation functionality.
