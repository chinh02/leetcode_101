# You are given an integer array nums of length n.

# In one operation, choose any subarray nums[l...r] (0 <= l <= r < n) and replace each element in that subarray with the bitwise AND of all elements.

# Return the minimum number of operations required to make all elements of nums equal.

# A subarray is a contiguous non-empty sequence of elements within an array.

from functools import reduce
from operator import and_
from typing import List

nums = [2,2,3,1,4]

def minOperations(nums: List[int]) -> int:
    target = reduce(and_, nums)
        # If all elements are already equal to target, no operation needed
    if all(num == target for num in nums):
        return 0
    # Otherwise, we can always select the entire array in one operation
    return 1
print(minOperations(nums))
