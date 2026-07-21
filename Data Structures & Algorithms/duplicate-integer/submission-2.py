class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = []
        for num in nums:
            if num not in dupes:
                dupes.append(num)
            else:
                return True
        return False