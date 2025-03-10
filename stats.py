def get_number_of_words(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    return word_count

def get_number_of_letters(book_text):
    number_of_letters_dict = {}
    filtered_number_of_letters_dict = {}
    number_of_letters_list = "a"
    lowercase_text = book_text.lower()
    number_of_letters_list = list(lowercase_text)

    for char in number_of_letters_list:
        if char not in number_of_letters_dict:
            number_of_letters_dict[char] = 1
        else:
            number_of_letters_dict[char] += 1
    
    for char in number_of_letters_dict:
        if char.isalpha() == True:
            filtered_number_of_letters_dict[char] = number_of_letters_dict[char]
    
    list_of_keys = list(filtered_number_of_letters_dict.keys())
    list_of_keys.sort()
    sorted_number_of_letters_dict = {i: filtered_number_of_letters_dict[i] for i in list_of_keys}
    

    return sorted_number_of_letters_dict
    