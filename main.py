from stats import get_words, get_chars, formater
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    frankenstein = get_book_text(sys.argv[1])
    char_count = get_chars(frankenstein)
    word_count = get_words(frankenstein)
    return frankenstein, char_count, word_count
    

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)





print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
frankenstein, char_count, word_count = main()
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("----------- Char Count ----------")
formater(char_count)

