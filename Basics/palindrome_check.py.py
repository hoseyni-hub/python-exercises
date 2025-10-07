# week6_exercise7_palindrome_check.py
# This program checks if a given word is a palindrome

def is_palindrome(word):
    return word == word[::-1]

# Example
text = input("Enter a word: ")
if is_palindrome(text):
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
