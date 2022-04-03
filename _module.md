# Python Coding

* ### [Menu](./README.md)
* ### Module
    * [Argument Parsing](#p1)
    * [Collections Module - ChainMap, Counter, defaultdict, deque](#p2)

<br />

## Argument Parsing                                 <a name="p1"></a>
```python
# Initialization

import argparse

parser = argparse.ArgumentParser(
         description="A simple argument parser",
         epilog="This is where you might put example usage"
        )
 
parser.print_help()

"""
usage: main.py [-h]

A simple argument parser

optional arguments:
  -h, --help  show this help message and exit

This is where you might put example usage
"""
```

```python
import argparse

parser = argparse.ArgumentParser(
    description='A simple argument parser',
    epilog='This is where you might put example usage'
)

# Required argument
parser.add_argument('-x', help='Help text for option X', action="store", required=True)

# Mutually Exclusive Group
group = parser.add_mutually_exclusive_group()

# Optional arguments
group.add_argument( '-y', help='Help text for option Y', default=False, type=bool)
group.add_argument('-z', help='Help text for option Z', type=int)

parser.print_help()

"""
usage: tempvbbajeo.py [-h] -x X [-y Y] [-z Z]

A simple argument parser

optional arguments:
-h, --help  show this help message and exit
-x X        Help text for option X
-y Y        Help text for option Y
-z Z        Help text for option Z

This is where you might put example usage
"""

print(parser.parse_args())
```

<br />

## Collections Module                               <a name="p2"></a>
### 1. ChainMap
```python
"""
ChainMap: With precendence when initialization
"""

import argparse
from collections import ChainMap

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

default = Namespace(model1="Ford", model2="Chevy")

parser = argparse.ArgumentParser()
parser.add_argument('-model3')
parser.add_argument('-model4')
args = parser.parse_args()

# 'For object has __dict__ attribute: vars(args)' equals 'args.__dict__'
car_model       = {key: value for key, value in vars(args).items() if value}
# Use ChainMap to gather two dicts, then convert back to dict for further ChainMap execution
car_model       = dict(ChainMap(car_model, {key: value for key, value in vars(default).items() if value}))

car_parts       = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options     = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}

car_pricing = ChainMap(car_model, car_accessories, car_options, car_parts)
print(car_pricing)

"""
> python3 ___.py -model3 Mercedes

ChainMap(
            {'model1': 'Ford', 'model2': 'Chevy', 'model3': 'Mercedes'}    # car_model
            {'hood_ornament': 150, 'seat_cover': 99, 'cover': 100},        # car_accessories
            {'rollbar': 300, 'A/C': 1000, 'Turbo': 2500},                  # car_options
            {'engine': 5000, 'hood': 500, 'front_door': 750}               # car_parts
        )
"""
```

### 2. Counter
```python
"""
Counter: With handful methods - elements(), most_common(), subtract(), update()
"""

from collections import Counter

# Initialize / elements() / most_common()
counter = Counter('superfluous')
print(counter)                          # Counter({'u': 3, 's': 2, 'e': 1, 'f': 1, 'l': 1, 'o': 1, 'p': 1, 'r': 1})
iterator = counter.elements()           # <itertools.chain object at 0x105ca9b50>
print(list(counter.elements()))         # ['e', 'f', 'l', 'o', 'p', 's', 's', 'r', 'u', 'u', 'u']
while iterator: print(next(iterator))   # e, f, l, o, p, s, s, r, u, u, u
print(counter['u'])                     # 3
print(counter.most_common(3))           # [('u', 3), ('s', 2), ('e', 1)]

# subtract()
tmp = Counter('super')
counter.subtract(tmp)
print(counter)                          # Counter({'u': 2, 'f': 1, 'l': 1, 'o': 1, 's': 1, 'e': 0, 'p': 0, 'r': 0})
print(counter['u'])                     # 2
print(counter['p'])                     # 0

# Update()
counter.update(tmp)
print(counter)                          # Counter({'u': 3, 's': 2, 'e': 1, 'f': 1, 'l': 1, 'o': 1, 'p': 1, 'r': 1})
```

```python
"""
defaultdict: Can set default using lambda / None for KeyError
"""

from collections import defaultdict

# int
table = defaultdict(int)
words = 'Hello World'.split(' ')
for word in words: table[word] += 1
print(table)            # defaultdict(<type 'int'>, {'World': 1, 'Hello': 1})

# list
table = defaultdict(list)
data  = [(1234, 100.23), (345, 10.45), (1234, 75.00), (345, 222.66), (678, 300.25), (1234, 35.67)]
for key, value in data: table[key].append(value)
print(table)            # defaultdict(<type 'list'>, {345: [10.45, 222.66], 1234: [100.23, 75.0, 35.67], 678: [300.25]})

# lambda
table = defaultdict(lambda: 'Foo Fighters')
table['Mike'] = 'Aerosmith'
table['Jerry']          # Foo Fighters
print(table)            # defaultdict(<function <lambda> at 0x100a888d0>, {'Mike': 'Aerosmith', 'Jerry': 'Foo Fighters'})

# None = KeyError
table = defaultdict(None)
table['Mike']           # KeyError: 'Mike'
```

``python

```