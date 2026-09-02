class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)

        left = 0
        right = length -1

        while left < right:
            current_nums = numbers[left] + numbers[right]

            if current_nums == target:
                return [left+1, right + 1 ]

            elif current_nums < target:
                left += 1

            else:
                right -= 1
        
        return []

        