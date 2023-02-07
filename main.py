"""
Author  : Yuan-Yao Lou (Mike)
Title   : PhD student in ECE at Purdue University
Email   : yylou@purdue.edu
Website : https://yylou.github.io/
Date    : Feb 05, 2023

Project :
    [Coding practice] Interative-mode
"""

import argparse                 as ARGU
import inspect

from Array                      import Array
from Test                       import Test
from parse                      import Company

def argu():
    parser = ARGU.ArgumentParser(description="LeetCode Problem Solving DB")
    parser.add_argument("-prob",     nargs='?', type=str,    default="",    help="(problem id)")
    return parser

def get_test(id: str): Test.search(id)
def get_code(id: str): print('\n\n' + inspect.getsource(Array.search(id)))

def main():
    argp = argu().parse_args()
    if argp.prob:
        get_code(argp.prob)
        get_test(argp.prob)

if __name__ == "__main__":
    main()