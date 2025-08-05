from typing import List

nums = [5, 3, 8, 3, 9, 1, 5, 3]

def insertion_sort(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        # Move elements of nums[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

print(insertion_sort(nums))