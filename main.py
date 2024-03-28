
def main():
    book_path = "books/frankenstein.txt"
    book = get_books(book_path)
    book_word_count = number_of_words(book)
    char_count_dict = count_letters(book)
    char_sorted_list = char_dict_sort(char_count_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {book_word_count} words found in the book.")
    for entry in char_sorted_list:
        if entry["char"].isalpha():
            print(f"The {entry["char"]} character was found {entry["num"]} times")

    print("---End of Report ---")

def sort_on(dict):
    return dict["num"]

def char_dict_sort(char_count_dict):
    sorted = []
    for char in char_count_dict:
        sorted.append({"char": char, "num": char_count_dict[char]})
        sorted.sort(reverse=True, key=sort_on)
    return sorted

def get_books(book_path):
    with open(book_path) as f:
        return f.read()

def number_of_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    chars = {}
    for c in text:
        lowered_string = c.lower()
        if lowered_string in chars:
            chars[lowered_string] += 1
        else:
            chars[lowered_string] = 1
    return chars

main()