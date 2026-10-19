class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mymap = {}
        # input the nums into an a map where the key is a specific number after having seen that key we update it's value for how many times we have seen it 
        for num in nums:
            if num in mymap: 
                mymap[num] += 1
            else: 
                mymap[num] = 1
        result = []
        
        # We want the top 'k' elements, so we run this loop 'k' times
        for _ in range(k):
            max_freq = 0
            best_key = None
            
            # .items() lets you loop through both the keys and values at the same time
            for key, val in mymap.items():
                if val > max_freq:
                    max_freq = val
                    best_key = key
            
            # We found the highest current frequency! Add the key to our result list
            result.append(best_key)
            
            # Remove this key from the map so the next loop finds the *next* highest
            mymap.pop(best_key)
            
        return result
            


            
           