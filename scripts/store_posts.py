# O(n) Space Complexity (Storing all posts)
def store_posts(n):
    """ Creates a list storing all posts in memory,
    consuming extra space. """
    posts = []
    for i in range(n):
        posts.append(f"Post {i}")  # Extra memory used
    return posts

print(store_posts(5))
