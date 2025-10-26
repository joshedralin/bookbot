from stats import get_num_words
from stats import count_char
from stats import sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    file_path = "books/frankenstein.txt"
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
