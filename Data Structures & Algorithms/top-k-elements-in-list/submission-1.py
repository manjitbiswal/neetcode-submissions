
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        heap = []
        count= Counter(nums)

        for n in count:
            heapq.heappush(heap,(-count[n],n))
        result = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)
        return result



        