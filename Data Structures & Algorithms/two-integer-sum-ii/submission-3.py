class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            # if left + right = target, retrun left, right
            numsum = numbers[left] + numbers[right]
            if numsum == target:
                return [left+1, right+1]
            elif numsum > target:
                right -= 1
            else: 
                left += 1
                continue

        return []

                       

