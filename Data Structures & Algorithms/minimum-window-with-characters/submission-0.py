class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(t) > len(s) or t == ""):
            return ""
        countT = {}
        countS = {}
        res = ""
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        have, need = 0, len(countT)
        res, reslen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            countS[c] = countS.get(c, 0) + 1
            if c in countT and countS[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if reslen != float("infinity") else ""