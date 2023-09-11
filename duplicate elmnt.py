# Program to print the duplicate elements of an array

arr = [1,2,3,4,5,6,1,2];

print("Duplicate elements in given array: ");
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] == arr[j]):
            print(arr[j]);


            # Duplicate elements can be found using two loops. The outer loop will iterate through the array from 0 to length of the array. The outer loop will select an element.
            # The inner loop will be used to compare the selected element with the rest of the elements of the array.