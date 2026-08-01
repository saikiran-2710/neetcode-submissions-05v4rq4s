class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        s=bin(n)
        for i in range(len(s)):
            if s[i] == '1':
                count+=1
        return count
        