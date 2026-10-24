
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
            result.append(heapq.heappop(heap)[1])
        return result



        