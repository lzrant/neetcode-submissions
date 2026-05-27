class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0: 
            return None
        l, r = 0,len(numbers) - 1
        l3 = []
        for i in range(len(numbers)):
            if numbers[l] + numbers[r] == target and l < r: 
                l3.append(l+1)
                l3.append(r+1)
                return l3
            elif numbers[l] + numbers[r] > target and l < r: 
                r -=1
            elif numbers[l] + numbers[r] < target and l < r: 
                l +=1
            
                
        return l3 







# if numbers[l] == numbers[r]: 
            #     return None
            # if numbers[l] + numbers[r] == target and l < r: 
            #     l3.append(numbers[l]) 
            #     l3.append(numbers[r])
            #     return l3
            # else: 
            #     l += 1
            #     r += 1