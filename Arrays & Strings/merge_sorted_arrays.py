def merge_sorted_arrays(array_1, array_2):
    if len(array_1) == 0:
        return array_2

    if len(array_2) == 0:
        return array_1

    merged_array = []

    ind_1 = 0
    ind_2 = 0

    while ind_1 <= len(array_1) - 1 and ind_2 <= len(array_2) - 1:
        # array_1 val < array_2 val
        if array_1[ind_1] < array_2[ind_2]:
            merged_array.append(array_1[ind_1])
            ind_1 += 1

        # array_1 val > array_2 val
        elif array_1[ind_1] > array_2[ind_2]:
            merged_array.append(array_2[ind_2])
            ind_2 += 1

        # array_1 val and array_2 vals are equal
        else:
            merged_array.append(array_1[ind_1])
            merged_array.append(array_2[ind_2])
            ind_1 += 1
            ind_2 += 1

    # if ind_1 < len(array_1) - 1:
    #     merged_array.extend(array_1[ind_1:])
    #
    # if ind_2 < len(array_2) - 1:
    #     merged_array.extend(array_2[ind_1:])

    if ind_1 < len(array_1) - 1:
        for val in array_1[ind_1:]:
            merged_array.append(val)

    if ind_2 < len(array_2) - 1:
        for val in array_2[ind_2:]:
            merged_array.append(val)

    return merged_array


def test_merging(arr_1, arr_2):
    print(f"Array 1 : {','.join([str(val) for val in arr_1])}")
    print(f"Array 2 : {','.join([str(val) for val in arr_2])}")
    print(f"Merged array : {','.join([str(val) for val in merge_sorted_arrays(array_1=arr_1, array_2=arr_2)])}")


def main():
    # Test case 1
    arr_1 = [1, 2, 3]
    arr_2 = [4, 5, 6, 7]
    test_merging(arr_1=arr_1, arr_2=arr_2)
    print("\n")

    # Test case 2
    arr_1 = []
    arr_2 = [1, 2, 3]
    test_merging(arr_1=arr_1, arr_2=arr_2)
    print("\n")

    # Test case 3
    arr_1 = [1, 2, 3]
    arr_2 = []
    test_merging(arr_1=arr_1, arr_2=arr_2)
    print("\n")

    # Test case 4
    arr_1 = []
    arr_2 = []
    test_merging(arr_1=arr_1, arr_2=arr_2)
    print("\n")

    # Test case 5
    arr_1 = [1, 2, 5, 7]
    arr_2 = [3, 4, 5, 7, 9, 21]
    test_merging(arr_1=arr_1, arr_2=arr_2)
    print("\n")


if __name__ == '__main__':
    main()
