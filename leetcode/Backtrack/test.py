from functools import reduce
import math
from typing import List


def totalBeauty(nums: List[int]) -> int:
    MODS = 10**9 + 7
    ans = 0
    def generate_subsequences(arr):
        result = []

        def helper(index, current):
            if len(current) > 0:
                result.append(current.copy())

            for i in range(index, len(arr)):
                if not current or arr[i] > current[-1]: 
                    current.append(arr[i])
                    helper(i + 1, current)
                    current.pop()

        helper(0, [])
        return result
    subsequences = generate_subsequences(nums)

    gcd_dict = {}
    for subsequence in subsequences:
        g = reduce(math.gcd, subsequence)
        gcd_dict[g] = gcd_dict.get(g, 0) + 1

    for key, value in gcd_dict.items():
        ans = (ans + key * value) % MODS

    return ans

nums = [1,2,3]
    
print(totalBeauty(nums))