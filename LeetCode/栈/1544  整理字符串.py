class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) <= 1:
            return s

        res = []

        for i in range(len(s)):
            if not res:
                res.append(s[i])
            else:
                if res[-1] != s[i] and res[-1].lower() == s[i].lower():
                    res.pop()
                else:
                    res.append(s[i])
        return ''.join(res)

s = "leEeetcode"
print(Solution().makeGood(s))


