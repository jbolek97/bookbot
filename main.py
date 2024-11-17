def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    counts = new_dict(text)
    list = tranformation(counts)
    list.sort(reverse=True, key=sort_on)
    print(list)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def new_dict(text):
    letter_counts = {}
    low = text.lower()
    for char in low:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts


def tranformation(dict):
    list_dict = []
    for name, num in dict.items():
        new_dict = {"name" : name, "num" : num}
        list_dict.append(new_dict)
    return list_dict

def sort_on(dict):
    return dict["num"]


main()