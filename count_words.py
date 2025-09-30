# Task: Write a program that counts how many times each word appears in a text.

def count_words(text):
    words = text.lower().split()
    word_count = {}

    for word in words:
        word = word.strip(".,!?")
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

if __name__ == "__main__":
    sample_text = "Hello world! This is a test. Hello again, world."
    result = count_words(sample_text)

    print("Word frequencies:")
    for word, count in result.items():
        print(f"{word}: {count}")	