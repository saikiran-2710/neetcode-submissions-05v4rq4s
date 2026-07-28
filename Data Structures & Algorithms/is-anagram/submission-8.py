class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs={}
        freqt={}
        for i in s:
            if i in freqs:
                freqs[i]+=1
            else:
                freqs[i]=1
        for i in t:
            if i in freqt:
                freqt[i]+=1
            else:
                freqt[i]=1
        return freqs == freqt


        