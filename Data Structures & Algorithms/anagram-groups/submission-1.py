class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana= {}
        for s in strs:
            key = ''.join(sorted(s))
            ana.setdefault(key,[]).append(s)
        result = []
        for val in ana.values():
            result.append(val)
        return result
            
            
        