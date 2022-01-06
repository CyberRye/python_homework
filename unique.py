

def compress(list):
    return [1,2,3]

if __name__ == '__main__':
    expected_sorted = [(1, 2), (2, 1), (3, 1)]
    actual_sorted = sorted(compress([1, 2, 1, 3]))
    # assert expected_sorted == actual_sorted

    foos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(foos[0:10:2])

    bars = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    print(bars[1:10:2])