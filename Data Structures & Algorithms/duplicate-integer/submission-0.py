class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashyhashy = set()
        for n in nums: 
            if (n in hashyhashy):
                return True
            hashyhashy.add(n)
        return False

        
        
