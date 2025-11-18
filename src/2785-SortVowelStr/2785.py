class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('AEIOUaeiou')
        vowel_chars = sorted([c for c in s if c in vowels], key=lambda x: ord(x))
        result = []
        vowel_index = 0
        
        for char in s:
            if char in vowels:
                result.append(vowel_chars[vowel_index])
                vowel_index += 1
            else:
                result.append(char)
                
        return ''.join(result)# Solution
