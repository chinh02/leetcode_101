# You are given an integer array weight of length n, representing the weights of n parcels arranged in a straight line. A shipment is defined as a contiguous subarray of parcels. A shipment is considered balanced if the weight of the last parcel is strictly less than the maximum weight among all parcels in that shipment.

# Select a set of non-overlapping, contiguous, balanced shipments such that each parcel appears in at most one shipment (parcels may remain unshipped).

# Return the maximum possible number of balanced shipments that can be formed.


from typing import List


weight = [2,5,1,4,3,3,5,2,3,2]


def maxBalancedShipments(weight: List[int]) -> int:
    result = 0
    n = len(weight)
    current_max = weight[0]
    for right in range(1,n):
        current_max = max(current_max, weight[right])
        if weight[right] < current_max:
            result += 1
            current_max = -1
    return result

print(maxBalancedShipments(weight))