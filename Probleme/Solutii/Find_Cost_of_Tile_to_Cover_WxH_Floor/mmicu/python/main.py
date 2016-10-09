#!/usr/bin/env python3
"""
Calculate the total cost of tile it would take to cover a floor
plan of width and height, using a cost entered by the user.
"""
from __future__ import print_function

import argparse
import sys


class App(object):
    """Application."""

    def __init__(self, args):
        self._raw_args = args
        self._args = None
        self._argparse = argparse.ArgumentParser(
            description="Calculate Fibbonaci numbers ...")

        self.prepare_parser()

    def prepare_parser(self):
        """Prepare Argument Parser."""
        self._argparse.add_argument(
            "w", type=int, help="Width")
        self._argparse.add_argument(
            "h", type=int, help="Height")
        self._argparse.add_argument(
            "c", type=float, help="Cost of Tile assuming that a tile is 1x1")

    def run(self):
        """Run the application."""
        self._args = self._argparse.parse_args(self._raw_args)
        rez = App.get_cost(self._args.w, self._args.h, self._args.c)
        output = "The cost is : {}".format(rez)
        print(output)

    @staticmethod
    def get_cost(widht, height, cost):
        """Compute the cost."""
        return (widht * height) * float(cost)

if __name__ == "__main__":
    App(sys.argv[1:]).run()
