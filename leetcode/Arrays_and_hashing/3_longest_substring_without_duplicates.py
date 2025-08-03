# Given a string s, find the length of the longest substring without duplicate characters.

s = 'abcabcdx'

def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    n = len(s)
    result = 0
    for right in range(n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        result = max(result, right-left+1)
    return result

print(lengthOfLongestSubstring(s))