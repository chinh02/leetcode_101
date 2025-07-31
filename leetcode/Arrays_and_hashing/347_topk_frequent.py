from collections import Counter
import heapq

def topKFrequent(nums, k):
    # Step 1: Count frequencies
    count = Counter(nums)
    
    # Step 2: Build a max heap using negative frequencies
    max_heap = [(-freq, num) for num, freq in count.items()]
    print(count)
    print(max_heap)
    heapq.heapify(max_heap)
    
    # Step 3: Extract the top k elements
    result = [heapq.heappop(max_heap)[1] for _ in range(k)]
    
    return result

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))  # Output: [1, 2]