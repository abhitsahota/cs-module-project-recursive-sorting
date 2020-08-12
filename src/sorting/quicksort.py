import time

def partition(numbers): # helper function
    pivot = numbers[0]
    right = []
    left = []

    for num in numbers[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return pivot, right, left

def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot, right, left = partition(numbers)

    sorted = quicksort(left) + [pivot] + quicksort(right)

    return sorted

print(time.time(), quicksort([1,6,7,8,2,3,5,7,9,4]))