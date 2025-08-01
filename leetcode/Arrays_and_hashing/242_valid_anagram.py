from typing import List

s = "abcdef"
t = "dabcfe"

def isAnagram(s: str, t:str) -> bool:
    if len(s) != len(t):
        return False
        
    s_count = {}
    t_count = {}
    
    for i in range(len(s)):
        s_count[s[i]] = 1 + s_count.get(s[i], 0)
        t_count[t[i]] = 1 + t_count.get(t[i], 0)
    
    return s_count == t_count

print(isAnagram(s,t))