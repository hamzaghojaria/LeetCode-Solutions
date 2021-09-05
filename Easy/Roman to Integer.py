class Solution:
    def romanToInt(self,s: str) -> int:
    # Dictionary of roman numerals
        roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # This variable will store result
        num = roman_dic[s[len(s) - 1]]
    # Loop for each character from right to left
        for i in range(len(s) -1):
        # Check if the character at right of current character is bigger or smaller
            if roman_dic[s[i]] >= roman_dic[s[i + 1]]:
                num += roman_dic[s[i]]
            else:
                num -= roman_dic[s[i]]
        return num
        
