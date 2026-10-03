from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for right in range(len(nums)):

            # 1. Remove smaller numbers
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # 2. Add current index
            q.append(right)

            # 3. Remove index outside the window
            if q[0] <= right - k:
                q.popleft()

            # 4. Record maximum when window is ready
            if right >= k - 1:
                result.append(nums[q[0]])

        return result