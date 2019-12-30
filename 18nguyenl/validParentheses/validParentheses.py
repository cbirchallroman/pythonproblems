class Solution:
    def isValid(self, s: str) -> bool:
        characters = []
        
        parentheses = {"(": ")", "{": "}", "[": "]"}
        
        for c in s: # O(n)
            if c in parentheses: # O(1)
                characters.append(c)
            elif not (not characters): # O(1)
                if parentheses[characters[-1]] == c:
                    characters.pop()
                else:
                    return False
            else:
                return False
                
        if not characters: # O (1)
            return True
        
        return False
        