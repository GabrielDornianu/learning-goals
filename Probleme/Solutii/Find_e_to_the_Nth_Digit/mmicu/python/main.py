#!/usr/bin/env python3
"""
Enter a number and the program will generate `e`
up to that many decimal places.
"""
from __future__ import print_function

import argparse
import decimal
import functools
import sys


class App(object):
    """Application."""
    _MAX_ACCURACY = 100
    _MIN_ACCURACY = 2
    _STEPS_FOR_DECIMAL = 200

    def __init__(self, args):
        self._raw_args = args
        self._args = None
        self._argparse = argparse.ArgumentParser(
            description="Calculate e ...")

        self.prepare_parser()

    def prepare_parser(self):
        """Prepare Argument Parser."""
        self._argparse.add_argument(
            "accuracy", type=int, help="Number of decimal places.")

    def run(self):
        """Run the application."""
        self._args = self._argparse.parse_args(self._raw_args)

        if self._args.accuracy > self._MAX_ACCURACY:
            print("Max accuracy {}!".format(self._MAX_ACCURACY))
        elif self._args.accuracy < self._MIN_ACCURACY:
            print("Min accuracy {}".format(self._MIN_ACCURACY))
        else:
            accuracy = self._args.accuracy
            self.warning(accuracy)
            print("e :{}".format(str(self.get_e(accuracy))[:accuracy+2]))

    @staticmethod
    def warning(accuracy):
        """Print some warning if the computing will take a lot of time."""
        if accuracy > 20:
            print("WARNING: It may take some time!")

    @staticmethod
    def factorial(item):
        """Retrun factorial of item."""
        if not item:
            return 1
        return functools.reduce(lambda x, y: x*y, range(1, item+1), 1)

    @staticmethod
    def get_e(accuracy):
        """Get e calculated up to `accuracy` decimal places."""
        decimal.getcontext().prec = App._MAX_ACCURACY

        start = decimal.Decimal(1)
        for iteration in range(1, accuracy*App._STEPS_FOR_DECIMAL):
            start += decimal.Decimal(1) / decimal.Decimal(
                App.factorial(iteration))
        return start

if __name__ == "__main__":
    App(sys.argv[1:]).run()
