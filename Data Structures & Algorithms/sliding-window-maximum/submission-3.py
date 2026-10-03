from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for right in range(len(nums)):
        # remove the smaller num
            while q and nums[q[-1]] <= nums[right]:
                q.pop()

            # add nums in q
            q.append(right)

            # remove the out window
            if q[0] <= right - k:
                q.popleft()
            
            # add num if the window is ready
            if right >= k - 1:
                result.append(nums[q[0]])
        
        return result