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

def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
    char_list = []
    
    for item in char_dict:
        value = char_dict[item]
        char_list.append({"char": item, "num": value})
        
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
