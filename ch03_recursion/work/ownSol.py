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
fib_sohrt = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)

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
