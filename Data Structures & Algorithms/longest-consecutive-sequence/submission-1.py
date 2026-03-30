class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        new=sorted(set(nums))
        count=1
        longest=1

        for i in range(1,len(new)):
            if new[i] == new[i-1]+1:
                count+=1
            else:
                count = 1
            longest=max(longest,count)
        return longest

        


        