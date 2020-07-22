# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # Your code here
    while len(arrA) > 0 or len(arrB) > 0:
        if len(arrA) == 0:
            merged_arr.extend(arrB)
            break
        elif len(arrB) == 0:
            merged_arr.extend(arrA)
            break
        elif arrA[0] <= arrB[0]:
            merged_arr.append(arrA.pop(0))
            # merged_arr.append(arrB.pop(0))
        elif arrA[0] >= arrB[0]:
            merged_arr.append(arrB.pop(0))
            # merged_arr.append(arrA.pop(0))


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    if len(arr) > 1:
        middle = len(arr) // 2
        lhs = arr[:middle]
        rhs = arr[middle:]
        l = merge_sort(lhs)
        r = merge_sort(rhs)
        arr = merge(l, r)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#     pass


# def merge_sort_in_place(arr, l, r):
#     # Your code here
#     pass

print(merge([1,3,5], [2,4,6,9,10, 34]))