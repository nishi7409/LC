class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        magazine_letters = collections.Counter(magazine)

        for char in ransomNote:
            if magazine_letters[char] <= 0:
                return False
            magazine_letters[char] -= 1
        return True