import bisect


def binary_search_bisect(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1


# Example Array
Example = [4, 9, 15, 21, 34, 57, 68, 91]

Number = int(input("Enter the number to search: "))

# Function Call
result = binary_search_bisect(Example, Number)

if result != -1:
    print("Element is present at index: ", str(result), ".")
else:
    print("Element is not present in array.")
