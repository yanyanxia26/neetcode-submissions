# THIS USES O(N) SPACE, SO IT FAILS THE O(1) RULE, BUT IT FIXES YOUR LOGIC
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {} # Stores {number: index}
        
        for i, num in enumerate(numbers):
            complement = target - num
            
            # 1. Checks if we've seen it BEFORE (prevents using the same element twice)
            if complement in seen:
                # 2. Returns 1-indexed INDICES, not values
                return [seen[complement] + 1, i + 1] 
            
            # 3. Saves the current number and its index
            seen[num] = i 