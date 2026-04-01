class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            pair = target-nums[i]
            if pair in dic:
                 return [dic[pair],i]
            else:
                dic[nums[i]]=i

                                                                                           