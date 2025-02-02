# Binary search allgorith
def binary_search(lst, target):
    lst.sort() # sort list items in ascending order
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low+high)// 2
        if lst[mid] == target:
            return f'{target} is found at index {mid}'
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return f'{target} is not found!'

# Test case 1
target = 10
numbers = [2, 4, 6, 8, 10, 12, 14]
print(binary_search(numbers, target))

# Test case 1
target = 5
numbers = [3, 2, 4, 5, 6, 8, 10, 12, 14] # unsorted list
print(binary_search(numbers, target))
