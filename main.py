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
import re                       as RE

from Array                      import Array
from String                     import String
from Stack                      import Stack
from Tree                       import Tree

from Test                       import Colors
from parse                      import Company
from Test                       import Test

def argu():
    parser = ARGU.ArgumentParser(description="LeetCode Problem Solving DB")
    parser.add_argument("-prob",     nargs='?', type=str,    default="",    help="(problem id)")
    parser.add_argument("-list",     action='store_true',                   help="(solved problems)")
    return parser

def get_code(data): print('\n\n' + inspect.getsource(data) if data else "")
def get_test(id: str, obj: object, func: object): Test.search(id, obj, func); print("")

def main():
    argp = argu().parse_args()
    data  = {}
    files = OS.listdir("./company")
    for file in files: data[file] = Company(path=f"./company/{file}")
    
    HIFREQ = Colors.Pattern(Colors.BOLD, Colors.TLRED, Colors.BBLACK)
    YELLOW = Colors.Pattern(Colors.BOLD, Colors.TYELLOW, Colors.BNONE)
    
    table = {
        "Dynamic Programming":  "DP",
        "Breadth-First Search": "BFS",
        "Depth-First Search":   "DFS",
        "Binary Search Tree":   "BST",
    }

    if argp.list:
        print(f"\n    {YELLOW}{'ID':^8} {'Title':^60} {'Level':<15}{'Tags':<50}{'Company'}{Colors.END}")
        print("    " + "=====" * 34)

        counter = 0
        for element in [Array, String, Stack, Tree]:
            for problem_id in element.__dict__:
                result = RE.match("_(\d*)_(.*)", problem_id)
                if result and result.groups()[0]:
                    counter += 1

                    idx = result.groups()[0]
                    info = {"company": {"amazon": 0, "apple": 0, "bloomberg": 0, "facebook": 0, "google": 0, "microsoft": 0}}
                    for name, company in data.items():
                        if idx in company.get_problems():
                            info |= company.get_problem(idx).__dict__
                            info["company"][name[:-5]] = info['freq'] / company.sorted[0].freq * 100
                            del info["freq"]
                    
                    if any([_ > 50 for _ in info["company"].values()]): 
                        print(f"    {HIFREQ}{idx:^8} {info['title']:60}{Colors.END} {info['level']:<15}", end="")
                    else: 
                        print(f"    {idx:^8} {info['title']:60} {info['level']:<15}", end="")
                    print(f"{' / '.join(sorted([table[_] if _ in table else _ for _ in info['tags'][:3]])):<50}", end="")
                    print(f"{' | '.join([k.capitalize()[:3] if v != 0 else '   ' for k, v in sorted(info['company'].items())])}")
            print("    " + "=====" * 34)
        print(f"      Total: {counter}")


    if argp.prob:
        #   | Collect
        info = {"company": []}
        for name, company in data.items():
            if argp.prob in company.get_problems():
                info |= company.get_problem(argp.prob).__dict__
                info["company"].append((name[:name.index(".html")], f"{info['freq'] / company.sorted[0].freq * 100:.2f}"))
                del info["freq"]

        #   | Output
        info["company"].sort(key=lambda x: eval(x[1]), reverse=True)
        CYAN = Colors.Pattern(Colors.BOLD, Colors.TCYAN,  Colors.BNONE)
        GREEN= Colors.Pattern(Colors.BOLD, Colors.TGREEN, Colors.BNONE)
        RED  = Colors.Pattern(Colors.BOLD, Colors.TRED,   Colors.BNONE)
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
            if average > 30: print(f"    {GREEN}|{'(Average)':^15}|  {RED}{average:>5.2f}%{END}  {GREEN}|{END}")
            else: print(f"    {GREEN}|{'(Average)':^15}|  {average:>5.2f}%  |{END}")
            
            obj, func = None, None
            if   Array.search(argp.prob):  obj, func = Array,  Array.search(argp.prob)
            elif String.search(argp.prob): obj, func = String, String.search(argp.prob)
            elif Stack.search(argp.prob):  obj, func = Stack,  Stack.search(argp.prob)
            elif Tree.search(argp.prob):   obj, func = Tree,   Tree.search(argp.prob)
            if obj and func:
                get_code(func)
                get_test(argp.prob, obj, func.__func__ if func else None)
            else: print("\n    Solution not found\n")

if __name__ == "__main__":
    main()