class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        definitions = {"}":"{", ")":"(", "]":"["}
        
        """
        [({})]
        [
        [(
        [({
        [({}
        """

        temp = list()
        for char in s:
            if char not in definitions:
                temp.append(char)
            else:
                if not temp or definitions[char] != temp[-1]:
                    return False
                temp.pop()
        return not temp