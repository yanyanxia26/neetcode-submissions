class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = set()
        l = 0

        for r, ch in enumerate(s):
            while ch in window:
                window.remove(s[l])
                l += 1

            window.add(ch)
            res = max(res, r-l+1)
        return res      
