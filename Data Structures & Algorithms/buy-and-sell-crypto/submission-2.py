class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        #  establish left and right pointers
        left,right = 0,1 
        # create max profit variable
        max_prof = 0
        # while right pointer is less then the length of prices 
        while right < len(prices):
            # if the prices at the left pointer are less then prices at the right pointer
            if prices[left] < prices[right]: 
                # then profit equals prices at the right - prices at the left
                profit = prices[right] - prices[left]
                # the max profit is set equal to whatever the maxmium difference between what 
                # we already have vs the new profit 
                max_prof = max(max_prof, profit)
                # else if the prices at the left are not less than the right 
                # we increment both pointers to the right 
            else:
                left = right
            right += 1
            # we then return the max profit at the end 
        return max_prof





