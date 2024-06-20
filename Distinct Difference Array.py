class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0,len(nums)):
            suffix = len(set(nums[i+1:len(nums)])) #The set only allows one ocurrance of each value, we get every value from i+1 to n-1
            prefix = len(set(nums[0:i+1])) #Every value from 0 to i+1
            result.append(prefix-suffix)
        return result