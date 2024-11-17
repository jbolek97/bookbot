def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    low = lowercase(text)
    print(low)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def lowercase(text):
    lowercase_text = text.lower()
    return lowercase_text

main()