# You are given a string s of length n and an integer array order, where order is a permutation of the numbers in the range [0, n - 1].

# Starting from time t = 0, replace the character at index order[t] in s with '*' at each time step.

# A substring is valid if it contains at least one '*'.

# A string is active if the total number of valid substrings is greater than or equal to k.

# Return the minimum time t at which the string s becomes active. If it is impossible, return -1.
from typing import List

s = "abc"
order = [1,0,2]
k = 2

def minTime(s: str, order: List[int], k: int) -> int:
        def count_substrings_with_star(st):
            count = 0
            n = len(st)
        
            for start in range(n):
                for end in range(start + 1, n + 1):
                    substring = st[start:end]
                    if '*' in substring:
                        count += 1
        
            return count
        s = list(s)
        for i, o in enumerate(order):
            s[o] = '*'
            print(s)
            if count_substrings_with_star(s) > k: 
                return i
        return count_substrings_with_star(s)

print(minTime(s,order,k))