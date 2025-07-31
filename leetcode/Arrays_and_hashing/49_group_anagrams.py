from collections import defaultdict
from typing import List

strs = ["eat","tea","tan","ate","nat","bat"]


def groupAnagrams(strs: List[str]) -> List[List[str]]:    
    ans = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        ans[key].append(s)
    return list(ans.values())

print(groupAnagrams(strs))
