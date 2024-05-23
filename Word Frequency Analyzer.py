# word_frequency.py

from collections import Counter

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
        words = text.split()
        word_counts = Counter(words)
        return word_counts
    except FileNotFoundError:
        return "File not found"

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    word_counts = count_words(filename)
    if isinstance(word_counts, str):
        print(word_counts)
    else:
        for word, count in word_counts.most_common():
            print(f"{word}: {count}")
