class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        setnums=set(nums)

        for num in nums:
            if num -1 not in setnums:
                current = num
                count = 1
                while current + 1 in setnums:
                    current += 1 
                    count+=1
                longest = max(count,longest)
        return longest
        