from typing import List

nums = [100,4,200,1,3,2]


def longestConsecutive(nums: List[int]) -> int:
    result = 0
    num_set = set(nums)
    for num in nums:
        if (num - 1) not in num_set:
            current = 1
            while num + 1 in num_set:
                current +=1
                num +=1
            result = max(result, current)
    return result

print(longestConsecutive(nums))