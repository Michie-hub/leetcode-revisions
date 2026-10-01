## Top K Frequent Elements--Given an integer array nums and an integer k, return the k most frequent elements. Your algorithm's time complexity must be better tha O(n log n).
import heapq 
def top_k_frequent_elements(nums, k):
    count = {}
    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    heap = []        
    for n, freq in count.items():
        heapq.heappush(heap, (-freq, n))
    result = []
    for _ in range(k):
        freq, n = heapq.heappop(heap)
        result.append(n)
    return result
nums = [1,1,1,2,2,2,2,2,5]
k = 2
print(top_k_frequent_elements(nums, k))        
        
  ## O(n log n) not the most optimal
  #THE BUCKET SORT   
            
                