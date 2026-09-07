class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in subs:
                subs.remove(s[l])
                l += 1
            subs.add(s[r])
            res = max(res, r - l + 1)
        return res       