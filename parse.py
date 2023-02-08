"""
Author  : Yuan-Yao Lou (Mike)
Title   : PhD student in ECE at Purdue University
Email   : yylou@purdue.edu
Website : https://yylou.github.io/
Date    : Jan 22, 2023

Describtion : Parse HTML (Leetcode: Company tags)
"""

from bs4        import BeautifulSoup
import json     as      JSON

class Problem:
    def __init__(self, id=0, title="None", href="/", tags="None", level="Easy|Medium|Hard", freq="0.0"):
        self.id     = id
        self.title  = title
        self.href   = href
        self.tags   = tags
        self.level  = level
        self.freq   = freq
    
    def __str__(self): return JSON.dumps(self.__dict__, indent=4)

class Company:
    def __init__(self, path):
        self.object = BeautifulSoup(open(path, encoding="utf-8"), features="html.parser")
        self.table  = self.object.find("tbody", attrs={"class": "reactable-data"})
        self.id     = self.table.find_all("td", attrs={"label": "#"})
        self.title  = self.table.find_all("td", attrs={"label": "Title"})
        self.href   = [title.a for title in self.title]
        self.tags   = self.table.find_all("td", attrs={"label": "Tags"})
        self.level  = self.table.find_all("td", attrs={"label": "Difficulty"})
        self.freq   = self.table.find_all("td", attrs={"label": "Frequency,[object Object]"})
        self.filter = {"level": {},
                       "tags":  {}}
        self.problems = {}
        self.sorted = []
        for i in range(len(self.id)):
            id      = "0"*(4 - len(self.id[i].attrs["value"])) + self.id[i].attrs["value"]
            title   = self.title[i].attrs["value"]
            href    = f"https://leetcode.com{self.href[i].attrs['href']}"
            tags    = [tag.attrs["title"] for tag in self.tags[i].find_all("a")]
            level   = ' '.join(self.level[i].span.contents)
            freq    = self.freq[i].attrs["value"]
            
            self.problems[id] = Problem(id=id, title=title, href=href, tags=tags, level=level, freq=freq)
            self.sorted.append(Problem(id=id, title=title, href=href, tags=tags, level=level, freq=freq))
            
            self.filter["level"][level] = self.filter["level"].get(level, []) + [id]
            for tag in tags: self.filter["tags"][tag] = self.filter["tags"].get(tag, []) + [id]

    def get_problem(self, id: str): return self.problems[id]
    def get_problems(self): return [prob.id for prob in sorted(self.problems.values(), key=lambda x: x.freq, reverse=True)]
    def get_tags(self):     return [tag[0] for tag in sorted(self.filter["tags"].items(), key=lambda x: len(x[1]), reverse=True)]
    def get_levels(self):   return [(level[0], level[1]) for level in sorted(self.filter["level"].items(), key=lambda x: len(x[1]), reverse=True)]