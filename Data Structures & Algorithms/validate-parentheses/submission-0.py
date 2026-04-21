class Solution:
    def isValid(self, s: str) -> bool:
        # Setup the stack
        stack = []
        # set up the hashmap/dictionary 
        closeToOpen = {")":"(", "]": "[", "}":"{"}
        # loop through characters in string
        for c in s: 
            # if character is in the dictionary
            if c in closeToOpen:
                # then check if the stack and the stack at -1 equals 
                if stack and stack [-1] == closeToOpen[c]: 
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c) 
        return True if not stack else False 


    
