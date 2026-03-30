class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            key=tuple(sorted(string))
            if key in dic:
                dic[key].append(string)
            else:
                dic[key]=[string]
        return list(dic.values())
        