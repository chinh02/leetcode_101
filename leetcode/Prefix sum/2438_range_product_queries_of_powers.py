# # Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.

# You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.

# Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.

from typing import List


n = 15 
queries = [[0,1],[2,2],[0,3]]

def productQueries(n: int, queries: List[List[int]]):
    powers = []
    power = 1
    while n > 0:
        if n % 2 == 1:
            powers.append(power)
        power *= 2
        n //= 2
    answer = [] 
    for left,right in queries:
        current = 1
        for i in range(left, right + 1):
            current *= powers[i]
        answer.append(current)
    return answer

print(productQueries(15, queries))