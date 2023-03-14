class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        
        i = 0
        longest = 0
        sub = ""
        
        while i < len(s):
            if s[i] not in sub:
                sub = sub + s[i]
                longest = max(longest, len(sub))
            else:
                sub = sub[sub.index(s[i]) + 1:] + s[i]
            i += 1
        return longest
            