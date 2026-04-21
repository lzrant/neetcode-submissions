class Solution:

    def encode(self, strs: List[str]) -> str:
        # turn list into a string 
        # for every string 

        h = ""
        for s in strs: 
            h += f"{len(s)}#{s}" 
        return h 
    def decode(self, s: str) -> List[str]:
        
        # return the original list of strings 
        i = 0 
        # count
        
        
        res = []
        count = 0 
        start = 0
        while i < len(s): 
            if s[i] == "#": 
                count = int(s[start : i])
                res.append(s[i+1 : i + count +1]) 
                start = i +count+1 
                i+= count + 1
            i+=1
            


        return res 
            