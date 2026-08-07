class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum=0
        maxsum=nums[0]
        for num in nums:
            if currentsum<0:
                currentsum=0
            currentsum+=num

            maxsum=max(currentsum,maxsum)
        return maxsum



        