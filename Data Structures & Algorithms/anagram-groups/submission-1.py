class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap = {}
        words = []
        for i in range(len(strs)): 
            words = "".join(sorted(strs[i]))
            if (words in mymap): 
                mymap[words] += [strs[i]]
            else: 
                mymap[words] = [strs[i]]
        return list(mymap.values())
