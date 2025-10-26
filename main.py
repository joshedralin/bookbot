import sys
from stats import get_num_words
from stats import count_char
from stats import sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    book_text = get_book_text(file_path)
    print(get_num_words(book_text))
    print("--------- Character Count -------")

    char_list = sort_dict(count_char(book_text))
    for item in char_list:
        if item["char"].isalpha():
            print (f"{item["char"]}: {item["num"]}")

    print("============= END ===============")
    
main()
