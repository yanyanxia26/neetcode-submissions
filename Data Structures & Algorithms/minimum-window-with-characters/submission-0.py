class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        have = 0
        need_len = len(need)

        window = {}
        left = 0
        result = [-1, -1]
        result_len = float("inf")
        for right in range(len(s)):
            c = s[right]

            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1
            
            while have == need_len:
                # window coved all t str
                if right - left + 1 < result_len:
                    result = [left, right]
                    result_len = right - left + 1
                
                # Shrink the window
                c = s[left]
                window[c] -= 1

                if c in need and window[c] < need[c]:
                    have -= 1
                
                left += 1
        left, right = result

        return s[left:right + 1]
