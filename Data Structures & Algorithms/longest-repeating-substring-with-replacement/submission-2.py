class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # XYYX, k = 2
        # replace YY with X to create a str of length 4 where each c in s is the same
        left = 0
        counts = {}
        max_freq = 0
        res = 0
        
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(max_freq, counts[s[right]])
        
            while(right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1) 
        return res

            
        