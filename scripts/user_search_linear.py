# Linear Search (O(n))
def search_user_linear(users, target):
    """ Searches for a user in a list 
    by checking each element one by one. """
    for user in users:
        if user == target:
            return "User found"
    return "User not found"

users_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(search_user_linear(users_list, "Charlie"))  # O(n)
