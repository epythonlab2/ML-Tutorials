# O(1) Space Complexity (No extra memory used)
def stream_posts(n):
    """ Streams posts directly without storing them, 
    using constant space. """
    for i in range(n):
        print(f"Post {i}")  # No extra storage

stream_posts(5)
