# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

from typing import List


fruits = [1,2,1]

def totalFruit(fruits: List[int]) -> int:
    n = len(fruits)
    left = 0
    fruit_dict = {}
    result = 0
    for right in range(n):
        fruit_dict[fruits[right]] = fruit_dict.get(fruits[right],0)+1
        while len(fruit_dict) > 2:
            left_fruit = fruits[left]
            fruit_dict[left_fruit] -= 1
            if fruit_dict[left_fruit] == 0:
                del fruit_dict[left_fruit]
            left += 1
        result = max(result, right - left + 1)
    return result

print(totalFruit(fruits))