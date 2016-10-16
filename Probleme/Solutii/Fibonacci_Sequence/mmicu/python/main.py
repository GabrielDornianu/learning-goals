#!/usr/bin/env python3
"""
Enter a number and the program will generate that number
of Fibonacci numbers
"""
from __future__ import print_function

import argparse
import sys


class App(object):
    """Application."""
    _MAX_COMPUTE = 10000
    _MIN_COMPUTE = 2

    def __init__(self, args):
        self._raw_args = args
        self._args = None
        self._argparse = argparse.ArgumentParser(
            description="Calculate Fibbonaci numbers ...")

        self.prepare_parser()

    def prepare_parser(self):
        """Prepare Argument Parser."""
        self._argparse.add_argument(
            "n", type=int, help="Number fibonacci numers.")

    def run(self):
        """Run the application."""
        self._args = self._argparse.parse_args(self._raw_args)

        if self._args.n > self._MAX_COMPUTE:
            print("Max numbers that can be generate {}!".format(
                self._MAX_COMPUTE))
        elif self._args.n < self._MIN_COMPUTE:
            print("Min numbers that can be generate {}!".format(
                self._MAX_COMPUTE))
        else:
            print(App.get_fib(self._args.n))

    @staticmethod
    def get_fib(number):
        """Generate `n` Fibonacci numbers."""
        buff = [1, 1]
        for i in range(2, number):
            buff.append(buff[i-1]+buff[i-2])

        return buff

if __name__ == "__main__":
    App(sys.argv[1:]).run()
