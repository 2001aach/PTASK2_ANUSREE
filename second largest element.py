# Find Second Largest Number in Array

# list = [1,2,3,4,5,]
# print("Second largest element is:", sorted(list)[-2])


def Second_Largest(arr):
    secondLargest = 0
    largest = min(arr)

    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        else:
            secondLargest = max(secondLargest, arr[i])

    return secondLargest

print(Second_Largest([1,4,8,6,9]))