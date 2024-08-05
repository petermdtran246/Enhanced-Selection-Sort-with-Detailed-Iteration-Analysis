def selection_sort_ascending(arr):
    """
    Sorts an array in ascending order using the selection sort algorithm

    :parameter
    ----------------------------------------------
        arr: The input array to be sorted
    """
    n = len(arr)

    for k in range(n):
        # Initialize counters for comparisons and swaps
        comparisons = 0
        swaps = 0

        # Find the minimum element in the unsorted part of the array
        min_index = k
        for i in range(k + 1, n):
            comparisons += 1  # Increment comparison count
            if arr[i] < arr[min_index]:
                min_index = i

        # Swap the found minimum element with the first element
        arr[min_index], arr[k] = arr[k], arr[min_index]
        swaps += 1 # Increment swap count

        # Print the current state of the array, comparisons, and swaps
        print(f'After iteration {k + 1}:')
        print(f'Partially sorted array: {arr}')
        print(f'Number of comparisons on this iteration: {comparisons}')
        print(f'Number of swaps: {swaps}')
        if k < n - 1:
            print('-' * 80)

# Problem instances
A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]

print('Sorting A1: ')
selection_sort_ascending(A1)
print('*' * 80)
print('\nSorting A2: ')
selection_sort_ascending(A2)
print('*' * 80)
print('\nSorting A3: ')
selection_sort_ascending(A3)