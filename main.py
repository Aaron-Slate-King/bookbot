from stats import get_number_of_words
from stats import get_number_of_letters
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
     
    book_text = get_book_text(sys.argv[1])

    number_of_words = get_number_of_words(book_text)
    number_of_letters = get_number_of_letters(book_text)
    return number_of_words, number_of_letters

character_dict = main()[1]

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print("Found " + str(main()[0]) + " total words")
print("--------- Character Count -------")
for char in character_dict:
    print(char + ": " + str(character_dict[char]))
print("============= END ===============")
