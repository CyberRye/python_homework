def merge(array1, array2):
    result = []
    temp1 = 0
    temp2 = 0
    # if at least iterator one array, then finish
    while len(array1) != temp1 + 1 or len(array2) != temp2 + 1:
        if array1[temp1] > array2[temp2]:
            result.append(array2[temp2])
            temp2 += 1
            if len(array1) == temp1:
                break
        else:
            result.append(array1[temp1])
            temp1 += 1
            if len(array2) == temp2:
                break
    print(len(array1), " ", temp1)
    if len(array1) != temp1:
        print(111)
        for i in range(len(array1) - temp1):
            result.append(array1[i])
    else:
        print(len(array2) - temp2)
        for i in range(len(array2) - temp2):
            result.append(array2[i])
    print("array result = ", result)


if __name__ == "__main__":
    print("hello")
    assert merge([1, 2, 7], [3]) == [1, 2, 3, 7]
    assert merge((3, 15), (7, 8)) == (3, 7, 8, 15)
