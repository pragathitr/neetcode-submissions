class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s2) < len(s1)):
            return False
        l = 0
        r = len(s1)
        while r <= len(s2):
            temp = s2[l : r]
            if collections.Counter(s1) == collections.Counter(temp):
                return True
            l += 1
            r += 1
        return False