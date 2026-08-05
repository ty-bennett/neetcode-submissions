class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # have two pointers for each element
        # iterate through whole list of nums 

        res = [1] * len(nums)

        # prefix prods
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res


     
      
