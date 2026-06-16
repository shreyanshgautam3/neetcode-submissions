class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = collections.Counter(s)
        b = collections.Counter(t)
        if a == b:
            if len(s) == len(t):
                return True
        return False