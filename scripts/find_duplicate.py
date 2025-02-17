# Find duplicates
# O(n^2) complixity - which is slow

def find_duplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                duplicates.append(nums[i])
    return duplicates
