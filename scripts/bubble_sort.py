def bubble_sort(lst):
    n = len(lst)
    
    for i in range(n):
        swapped=False  
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                swapped=True
        if not swapped:
            break

# Test case 1
lst = [64, 34, 25, 12, 22, 11, 90]
print(f'Original list:{lst}')
bubble_sort(lst)
print(f'Sorted list:{lst}')