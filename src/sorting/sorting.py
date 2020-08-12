import time

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    # starting at the beginning of `a` and `b`
    # compare the next value of each
    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] <= arrB[0]:
            # add smallest to `merged_arr`
            merged_arr.append(arrA[0])
            arrA = arrA[1:]
        else: 
            merged_arr.append(arrB[0])
            arrB = arrB[1:]

    while len(arrA) != 0:
            # add smallest to `merged_arr`
        merged_arr.append(arrA[0])
        arrA = arrA[1:]

    while len(arrB) != 0:
            # add smallest to `merged_arr`
        merged_arr.append(arrB[0])
        arrB = arrB[1:]

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        # print('left', left, 'right', right)

        # recursively call merge_sort() on LHS
        merge_sort(left)
        # recursively call merge_sort() on RHS
        merge_sort(right)
        # merge sorted pieces
        arr = merge(left, right)

    return arr

print(time.time(), merge_sort([1,6,7,8,2,3,5,7,9,4]))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

