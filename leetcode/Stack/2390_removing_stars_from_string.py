# You are given a string s, which contains stars *.

# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

# Input: s = "leet**cod*e"
# Output: "lecoe"


s = "leet**cod*e"

def removeStars(s: str) -> str:
        result = []
        for char in s:
            if char == "*":
                result.pop()
                continue
            else: result.append(char)
        return "".join(result)

print(removeStars(s))