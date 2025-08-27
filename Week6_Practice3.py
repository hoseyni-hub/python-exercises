# Week 6 - Day 2 - Practice 3
# Word Counter in a sentence

def word_count(sentence):
    words = sentence.split()
    return len(words)

# Example usage:
print(word_count("I am learning Python"))        # 4
print(word_count("GitHub is great for practice")) # 5
