
def main():
    book_path = "books/frankenstein.txt"
    book = get_books(book_path)
    book_word_count = number_of_words(book)
    print(f"There are {book_word_count} words found in the book.")
    char_counter = count_letters(book)
    print(char_counter)


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