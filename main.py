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
        for i in range(0, 3):
            print(list234[0][i])



for item in FlatIterator(nested_list):
    print(item)
