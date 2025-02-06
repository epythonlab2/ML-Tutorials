# Binary Search (O(log n))
def search_user_binary(users, target):
    """ Uses binary search to efficiently 
    find a user in a sorted list. """
    
    left, right = 0, len(users) - 1
    while left <= right:
        mid = (left + right) // 2
        if users[mid] == target:
            return "User found"
        elif users[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "User not found"

users_list = sorted(["Alice", "Bob", "Charlie", "David", "Eve"])
print(search_user_binary(users_list, "Charlie"))  # O(log n)
