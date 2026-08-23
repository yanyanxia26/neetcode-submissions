from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_tuple = Counter(nums)

        nums_maps = nums_tuple.most_common(k)
        return [num for num, _ in nums_maps]
        