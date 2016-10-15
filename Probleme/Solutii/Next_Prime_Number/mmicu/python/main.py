#!/usr/bin/env python3
"""
Have the program find prime numbers until the user
chooses to stop asking for the next one
"""
from __future__ import print_function
import math

from six import moves


def is_prime(number):
    """Check if a number is prime, the slow way.

    :rtype bool:
    """
    if number <= 1:
        return False
    for index in moves.range(2, int(math.sqrt(number))+1):
        if number % index == 0:
            return False
    return True

if __name__ == "__main__":
    PRIME = 1
    INP = "y"
    while INP.lower() != "n":
        PRIME += 1
        while not is_prime(PRIME):
            PRIME += 1
        print("Prime : {}".format(PRIME))
        INP = "n"
        INP = moves.input("Next prime ?[y/N] :")

    print("Done !")
