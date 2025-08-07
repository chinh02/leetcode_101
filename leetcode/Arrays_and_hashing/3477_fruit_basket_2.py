
from typing import List

fruits = [4,2,5]
baskets = [3,5,4]


def numOfUnplacedFruits(fruits: List[int], baskets: List[int]) -> int:
    n, count = len(fruits), 0
    for i in range(n):
        for j in range(n):
            if fruits[i] <= baskets[j]:
                count += 1
                baskets[j] = -1
                fruits[i] = float("inf")
    return n - count

print(numOfUnplacedFruits(fruits, baskets))