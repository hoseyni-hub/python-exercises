# Word Counter

def count_words(text):
    words = text.split()
    return len(words)

print("Word Counter Program")
user_text = input("Enter a sentence or paragraph: ")
word_count = count_words(user_text)

print(f"Your text contains {word_count} words.")