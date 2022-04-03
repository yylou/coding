# Python Coding

* ### [Menu](./README.md)
* ### Module
    * [Argument Parsing](#p1)
    * [Collections Module - ChainMap, Counter, defaultdict, deque, namedtuple, OrderedDict](#p2)

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

### 3. defaultdict
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

### 4. deque
```python
"""
deque: Generalization of stacks and queues
"""

from collections import deque
import string

def tail(filename, n=5):
    """
    Linux tail command for last n lines
    """
    try:
        with open(filename) as FILE:
            return deque(FILE, n)
    
    except OSError:
        print(f'Error opening file: {filename}')
        raise

queue = deque(string.ascii_lowercase)
print(queue)            # deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                        #        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

queue.append('A')       # deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                        #        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A'])

queue.appendleft('-')   # deque(['-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        #        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A'])

queue.rotate(1)         # deque(['A', '-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        #        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

queue.rotate(-1)        # deque(['-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        #        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A'])

queue.popleft()         # deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                        #        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A'])

queue.pop()             # deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                        #        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
```

### 5. namedtuple
```python
"""
namedtuple: Like a struct
"""

from collections import namedtuple

def getParameters1(**kwargs):
    for key, value in kwargs.items(): print(f'{key}={value}', end=', ')
    print()

def getParameters2(*args):
    print(args)

def getParameters3(ID, description, cost, amount):
    print(description)

def getParameters4(ID, description, *other):
    print(ID, description, other)

def getParameters5(ID, description, cost):
    print(ID, description, cost)


# First argument  = Class Name
# Second argument = field names
Parts = namedtuple('Parts', 'ID description cost amount')
auto_parts = Parts(ID='0001', description='Ford Engine', cost=1200.00, amount=10)

print(Parts)                # <class '__main__.Parts'>
print(auto_parts)           # Parts(ID='0001', description='Ford Engine', cost=1200.0, amount=10)
print(dir(Parts))           # [..., 'amount', 'cost', 'description', 'ID', ...]
print(dir(auto_parts))      # [..., 'amount', 'cost', 'description', 'ID', ...]

# Use dict keys to initialize
Parts = {'ID': '0001', 'description': 'Ford Engine', 'cost': 1200.00, 'amount': 10}
empty_parts = namedtuple('Parts', Parts.keys())

# Use keyword arguments (**kwargs) to fill in the values
# NOTE: *args give all parameters as a tuple
auto_parts  = empty_parts(**Parts)

print(Parts)                # {'amount': 10, 'cost': 1200.0, 'ID': '0001', 'description': 'Ford Engine'
print(empty_parts)          # <class '__main__.Parts'>
print(auto_parts)           # Parts(ID='0001', description='Ford Engine', cost=1200.0, amount=10)
print(dir(Parts))           # without 'amount', 'cost', 'description', 'ID'
print(dir(auto_parts))      # [..., 'amount', 'cost', 'description', 'ID', ...]

getParameters1(**Parts)     # ID=0001, description=Ford Engine, cost=1200.0, amount=10
getParameters2(*Parts)      # ('ID', 'description', 'cost', 'amount')
getParameters3(*Parts)      # description
getParameters4(*Parts)      # ID description ('cost', 'amount')
getParameters5(*Parts)      # TypeError: getParameters5() takes 3 positional arguments but 4 were given
```

### 6. OrderedDict
```python
"""
OrderedDict: Like a dict but preserves the order of insertion
"""

from collections import OrderedDict

data = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
orderedDict1 = OrderedDict(data)
orderedDict2 = OrderedDict(sorted(data.items()))

print(orderedDict1)         # OrderedDict([('orange', 2), ('pear', 1), ('banana', 3), ('apple', 4)])
print(orderedDict2)         # OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

print(orderedDict1.keys())  # ['orange', 'pear', 'banana', 'apple']
print(orderedDict2.keys())  # ['apple', 'banana', 'orange', 'pear']

```
