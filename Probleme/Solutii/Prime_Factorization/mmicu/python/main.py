#!/usr/bin/env python3
"""
Have the user enter a number and find all Prime Factors
(if there are any) and display them.
"""
from __future__ import print_function

import argparse
import sys


class App(object):
    """Application."""
    _MAX_COMPUTE = 10 ** 100
    _MIN_COMPUTE = - _MAX_COMPUTE

    def __init__(self, args):
        self._raw_args = args
        self._args = None
        self._argparse = argparse.ArgumentParser(
            description="Calculate Prime Factors ...")

        self.prepare_parser()

    def prepare_parser(self):
        """Prepare Argument Parser."""
        self._argparse.add_argument(
            "n", type=int, help="Number to find all prime factors")

    def run(self):
        """Run the application."""
        self._args = self._argparse.parse_args(self._raw_args)

        if self._args.n > self._MAX_COMPUTE:
            print("Max number we can use {}!".format(
                self._MAX_COMPUTE))
        elif self._args.n < self._MIN_COMPUTE:
            print("Max number we can use {}".format(
                self._MAX_COMPUTE))
        else:
            factors = App.get_factors(self._args.n)
            if factors:
                print("The prime factors are: {}".format(", ".join(factors)))
            else:
                print("There are no prime factors for {}".format(self._args.n))

    @staticmethod
    def get_factors(number):
        """Return a list with all prime factors of `number`."""
        number = abs(number)
        if number in [0, 1]:
            return []
        factors = []
        prime = 2
        while number != 1:
            if number % prime == 0:
                number = number / prime
                if prime not in factors:
                    factors.append(prime)
            else:
                prime += 1
        return [str(factor) for factor in factors]


if __name__ == "__main__":
    App(sys.argv[1:]).run()
