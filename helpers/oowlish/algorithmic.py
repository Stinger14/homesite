"""
Implement a function to determine if a given string is a palindrome 
(ignoring spaces, punctuation, and capitalization).
"""
import string

def is_palindrome(s):
    s_clean = s.lower()
    s_clean = ''.join([char for char in s_clean if char not in string.punctuation and char != ' '])

    return s_clean == s_clean[::-1] 

input_string1 = "A man, a plan, a canal, Panama!"
input_string2 = "racecar"

print(is_palindrome(input_string1))  # Should return True
print(is_palindrome(input_string2))  # Should return True
