class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        count = 0
        for center in range(2*size - 1):
            l = int(center / 2)
            r = l + center % 2
            while l >= 0 and r < size:
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1
        return count