from typing import List


nums = [5, 3, 8, 3, 9, 1, 5, 3]

def bubble_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):  # compare up to the unsorted part
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print(bubble_sort(nums))