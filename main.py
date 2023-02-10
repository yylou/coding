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
import bs4
import inspect
import json                     as JSON
import os                       as OS

from Array                      import Array
from Test                       import Test
from parse                      import Company

def argu():
    parser = ARGU.ArgumentParser(description="LeetCode Problem Solving DB")
    parser.add_argument("-prob",     nargs='?', type=str,    default="",    help="(problem id)")
    return parser

def get_code(data): print('\n\n' + inspect.getsource(data) if data else "")
def get_test(id: str): print('\n    """'); Test.search(id); print('    """\n')

def main():
    argp = argu().parse_args()
    if argp.prob:
        data  = {}
        files = OS.listdir("./company")
        for file in files: data[file] = Company(path=f"./company/{file}")

        info = {"company": []}
        for name, company in data.items():
            if argp.prob in company.get_problems():
                info |= company.get_problem(argp.prob).__dict__
                info["company"].append((name[:name.index(".html")], f"{info['freq'] / company.sorted[0].freq * 100:.2f}"))
                del info["freq"]

        info["company"].sort(key=lambda x: eval(x[1]), reverse=True)
        print(JSON.dumps(info, indent=4))



        get_code(Array.search(argp.prob))
        get_test(argp.prob)


if __name__ == "__main__":
    main()