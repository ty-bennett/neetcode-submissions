class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        seen = set()
        
        for n in num_set:
            if (n-1) not in seen:
                seen.add(n)
                length = 0
                while (n + length) in num_set:
                    seen.add(n + length)
                    length += 1
            longest = max(length, longest)
        return longest


            


        