# Open and read file contents
try:
    with open('data.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("""Error: File not found! 
          Please check the filename.""")
    
    
