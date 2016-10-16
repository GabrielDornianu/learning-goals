#!/usr/bin/env python3
"""
Enter a number and the program will generate PI
up to that many decimal places.
"""
from __future__ import print_function

import argparse
import decimal
import sys


class App(object):
    """Application."""
    _MAX_ACCURACY = 100
    _MIN_ACCURACY = 2
    _STEPS_FOR_DECIMAL = 4000

    def __init__(self, args):
        self._raw_args = args
        self._args = None
        self._argparse = argparse.ArgumentParser(
            description="Calculate PI ...")

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
            print("PI :{}".format(str(self.get_pi(accuracy))[:accuracy+2]))

    @staticmethod
    def warning(accuracy):
        """Display warning if accuracy is too high."""
        if accuracy > 20:
            print("WARNING: It may take some time!")

    @staticmethod
    def get_sign(place):
        """Get -1 or 1 depending if the place is even or odd."""
        return -1 if place % 2 == 0 else 1

    @staticmethod
    def get_pi(accuracy):
        """Get PI calculated up to `accuracy` decimal places."""
        decimal.getcontext().prec = App._MAX_ACCURACY

        start = decimal.Decimal(3)
        latest = 1
        for iteration in range(1, accuracy*App._STEPS_FOR_DECIMAL):
            base = decimal.Decimal(latest+1) * (latest+2) * (latest+3)
            start += App.get_sign(iteration) * (decimal.Decimal(4) / base)
            latest += 2

        return start

if __name__ == "__main__":
    App(sys.argv[1:]).run()
