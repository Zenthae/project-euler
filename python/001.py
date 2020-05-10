# -*- coding: UTF-8 -*-

"""
Project Euler, Problem 001 : Multiples of 3 and 5,

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer : 233168

"""


def MultiplesOf3And5(max):
    """
    Find the sum of all multiples of 3 or 5 below the max value.
    """
    sum = 0
    for x in range(max):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum


print(MultiplesOf3And5(1000))
