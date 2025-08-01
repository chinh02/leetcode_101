import re

s = "A man, a plan, a canal: Panama"
def isPalindrome(s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    i, j = 0, len(s)-1
    while (i<j):
        if(s[i]!=s[j]):return False
        i +=1
        j -=1
    return True

print(isPalindrome(s))
