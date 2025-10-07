# Palindrome Checker

def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

# Example usage:
print(is_palindrome("level"))   # True
print(is_palindrome("hello"))   # False
print(is_palindrome("Never odd or even"))  # True
