from nltk import flatten
from numpy import *

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


class FlatIterator(list):

    def __iter__(self):
        return self

    def __next__(self):
        list234 = []
        if len(self) == 0:
            raise StopIteration
        else:
            list234.append(self.pop(0))

        list123 = []
        for ar in list234[0]:
            list123.append(ar)

        return list123



nested_items = []
for item in FlatIterator(nested_list):
    for i in range(0, len(item)):
        nested_items.append(item[i])

print(nested_items)
