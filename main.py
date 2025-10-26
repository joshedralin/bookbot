from stats import get_num_words
from stats import count_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(get_num_words(book_text))
    print(count_char(book_text))

main()
