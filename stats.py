def get_num_words(string):
    temp_list = string.split()
    num_words = len(temp_list)
    
    return f"Found {num_words} total words"

def count_char(string):
    char_dict = {}
    for c in string:
        char = c.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict