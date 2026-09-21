class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if len(tokens) == 0: 
            return 0
        s = []
    # Checks for each token/item in tokens
        for token in tokens: 
            if token in {"+", "-", "*", "/"}: #if the item is one of the following operators  
                b = s.pop() #set b = to the pop
                a = s.pop() #set a = to the pop
                if token == "+": # if the token is == +
                    s.append(a + b) #append the answer of the pops
                elif token == "-": 
                    s.append(a - b)
                elif token == "*":
                    s.append(a*b) 
                elif token == "/": 
                    s.append(int((a/b)))
            else: 
                s.append(int(token))                #conver to integer append if the none of the previous have been met
        return s[0] #return the first item in the stack 
