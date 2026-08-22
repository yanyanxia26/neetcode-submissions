class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gAs = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key not in gAs:
                gAs[key] = []
            gAs[key].append(s)

        return list(gAs.values())
                


        