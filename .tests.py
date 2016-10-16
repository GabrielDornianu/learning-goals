# !/usr/bin/env python
"""
Run static code analysis.
"""
from __future__ import print_function

import atexit
import os
import subprocess


BAD_STRING = ["No config file found, using default configuration"]


def clean(results):
    """Clean results."""
    results = [item.strip() for item in list(results)]
    for string in BAD_STRING:
        while results.count(string):
            results.remove(string)
    return [item for item in results if item]


def python(path):
    """Run python analysis."""
    args = ["pylint", "-rn", path]
    process = subprocess.Popen(args, stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                               env=os.environ)
    results = clean(process.communicate())
    if results:
        atexit.register(exit, 1)
    if results:
        print("\n".join(results))


def html(path):
    """Run html analysis."""
    args = ["html_lint.py", "--disable=optional_tag", path]
    process = subprocess.Popen(args, stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                               env=os.environ)
    results = clean(process.communicate())
    if results:
        atexit.register(exit, 1)
    if results:
        print("\n".join(results))


def javascript(path):
    """Run js analysis."""
    args = ["jslint", path]
    process = subprocess.Popen(args, stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                               env=os.environ)
    results = clean(process.communicate())
    if results:
        atexit.register(exit, 1)
    if results:
        print("\n".join(results))

TESTS = {
    'py': [python],
    'js': [javascript],
    'html': [html],
}


def run(path):
    """Run tests depeing on the filetype."""
    print("Test :", path)
    ext = path.split('.')[-1]
    for test in TESTS.get(ext, []):
        test(path)


def start():
    """Start running tests."""
    for dirpath, _, filenames in os.walk('Probleme'):
        for filename in filenames:
            if not filename.startswith("."):
                run(os.path.join(dirpath, filename))

if __name__ == "__main__":
    exit(start())
