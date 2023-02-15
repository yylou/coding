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
import os                       as OS

from Array                      import Array
from String                     import String

from Test                       import Colors
from parse                      import Company
from Test                       import Test

def argu():
    parser = ARGU.ArgumentParser(description="LeetCode Problem Solving DB")
    parser.add_argument("-prob",     nargs='?', type=str,    default="",    help="(problem id)")
    return parser

def get_code(data): print('\n\n' + inspect.getsource(data) if data else "")
def get_test(id: str): Test.search(id); print("")

def main():
    argp = argu().parse_args()
    if argp.prob:
        data  = {}
        files = OS.listdir("./company")
        for file in files: data[file] = Company(path=f"./company/{file}")

        #   | Collect
        info = {"company": []}
        for name, company in data.items():
            if argp.prob in company.get_problems():
                info |= company.get_problem(argp.prob).__dict__
                info["company"].append((name[:name.index(".html")], f"{info['freq'] / company.sorted[0].freq * 100:.2f}"))
                del info["freq"]

        #   | Output
        info["company"].sort(key=lambda x: eval(x[1]), reverse=True)
        CYAN = Colors.Pattern(Colors.BOLD, Colors.TCYAN, Colors.BNONE)
        GREEN= Colors.Pattern(Colors.BOLD, Colors.TGREEN, Colors.BNONE)
        RED  = Colors.Pattern(Colors.BOLD, Colors.TRED, Colors.BNONE)
        GREY = Colors.Pattern(Colors.BOLD, Colors.TDGREY, Colors.BNONE)
        END  = Colors.END
        TAB  = "    "
        if "id" in info:
            print(f"\n\n{TAB}{CYAN}{info['id']}. {info['title']} ({info['href']}){END}")        # ID, Title, URL
            print(f"{TAB}{GREY}|  {info['level']}  |  {', '.join(info['tags'])}  |{END}")       # Level, tags
            for entry in info["company"]:
                if eval(entry[1]) > 50: print(f"    {GREEN}|{entry[0].capitalize():^15}|  {RED}{entry[1]+'%':>6}{END}  {GREEN}|{END}")
                else: print(f"    {GREEN}|{entry[0].capitalize():^15}|  {entry[1]+'%':>6}  |{END}")
            average = sum([eval(_[1]) for _ in info['company']]) / len(info['company'])
            if average > 30: print(f"    {GREEN}|{'(Average)':^15}|  {RED}{average:>5.2f}%{END}  {GREEN}|{END}", end="")
            else: print(f"    {GREEN}|{'(Average)':^15}|  {average:>5.2f}%  |{END}", end="")
            
            if   Array.search(argp.prob): get_code(Array.search(argp.prob))
            elif String.search(argp.prob): get_code(String.search(argp.prob))
            
            get_test(argp.prob)

if __name__ == "__main__":
    main()