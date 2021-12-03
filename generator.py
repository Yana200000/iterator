nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(list):
    for i in list:
        for b in range(0, 3):
            yield i[b]


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)
