from typing import List


nums = [1,2,3,1]

def containsDuplicate(nums: List[int]) -> bool:
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        else: num_set.add(num)
    return False


result = containsDuplicate(nums)
print(result)