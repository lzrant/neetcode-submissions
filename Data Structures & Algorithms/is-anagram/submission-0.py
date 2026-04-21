class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Hashmaps intialization
        countS, countT = {}, {} 
        # check first if the lengths of each string are different
        if (len(s)!= len(t)): 
            return False
        # loop through both hashmaps and compare them according to whatever value is at index i
        for i in range(len(s)): 
           countS[s[i]] = 1 + countS.get(s[i],0)
           countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT


        