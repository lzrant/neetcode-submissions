class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        my_list = []
        for i in range (len(strs)): 
            my_list = "".join(sorted(strs[i]))
            if (my_list in my_map): 
                my_map[my_list] += [strs[i]]
            else: 
                my_map[my_list] = [strs[i]] 

        return list(my_map.values())
        
    