def quickSort(sequence):
    if len(sequence) <= 1:
        return sequence
    left_list = []
    right_list = []
    pivot = sequence.pop()

    for item in sequence:
        if item < pivot:
            left_list.append(item)
        else:
            right_list.append(item)
    return quickSort(left_list)+[pivot]+quickSort(right_list)


print(quickSort([3, 1, 4, 1, 5, 9, 0, 2, 6, 5, 3, 5]))