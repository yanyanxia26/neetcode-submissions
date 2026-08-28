class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        prefix = [1] * length
        postfix = [1] * length

        for i in range(1, length):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in reversed(range(length -1)):
            postfix[i] = nums[i + 1] * postfix[i + 1]
        for i in range(length):
            res[i] = prefix[i] * postfix[i]
        
        return res