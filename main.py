def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(string):
    temp_list = string.split()
    num_words = len(temp_list)
    
    return f"Found {num_words} total words"
    
def main():
    print(count_words(get_book_text("books/frankenstein.txt")))

main()
