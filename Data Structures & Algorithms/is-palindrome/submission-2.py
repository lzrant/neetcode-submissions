class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for ch in s: 
            if ch.isalnum():
                a += ch.lower()
        if a == a[::-1]:
            return True 
        else: 
            return False
            

   

    