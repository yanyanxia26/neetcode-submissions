class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        left = 0
        right = len(numbers) - 1
        
        # Loop until the pointers meet
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Return 1-indexed positions
                return [left + 1, right + 1]
            elif current_sum < target:
                # The sum is too small. Because the array is sorted, 
                # moving the right pointer left would only make the sum smaller.
                # So, we MUST move the left pointer to the right to increase the sum.
                left += 1
            else:
                # The sum is too large. 
                # We MUST move the right pointer to the left to decrease the sum.
                right -= 1
                
        return []