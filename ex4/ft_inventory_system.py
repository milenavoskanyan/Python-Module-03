# import sys, sys.argv, len(), print(), sum(), list(), round(),
# dict.keys(), dict.values(), dict.update()

import sys

names = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "gregory",
    "John",
    "kevin",
    "Liam",
    "sophia"
]

list_all_upper = [name.capitalize() for name in names]
list_only_upper = [name for name in names if name[0].isupper()]

