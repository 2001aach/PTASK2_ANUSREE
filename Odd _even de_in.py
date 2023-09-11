# Sort even-placed elements in increasing and odd-placed in decreasing order


def even_odd(arr, n):
    evenArr = []
    oddArr = []

    for i in range(n):
        if ((i % 2) == 0):
            evenArr.append(arr[i])
        else:
            oddArr.append(arr[i])

    evenArr = sorted(evenArr)
    oddArr = sorted(oddArr)
    oddArr = oddArr[::-1]

    i = 0
    for j in range(len(evenArr)):
        arr[i] = evenArr[j]
        i += 1
    for j in range(len(oddArr)):
        arr[i] = oddArr[j]
        i += 1

arr = [0,1,2,3,4,5,6,7,8,9]
n = len(arr)
even_odd(arr, n)
for i in arr:
    print(i, end=" ")



# We create two auxiliary arrays even[] and odd[] respectively. We traverse input array and put all even-placed elements in even[] and odd placed elements in odd[]. Then we sort evenA[] in ascending and odd[] in descending order. Finally, copy even[] and odd[] to get theequired result.
