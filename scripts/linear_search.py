# Linear search example
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f'{target} is found at index {i}'
    
    return f'{target} is not found!'

# Test case 1
target = 7
arr = [2, 3, 8, 7, 9]
print(linear_search(arr, target))

# Test case 2
target = 10
arr = [4, 5, 8, 9, 2, 1]
print(linear_search(arr, target))