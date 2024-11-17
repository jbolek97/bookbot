def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        length = len(words)
    print(length)

main()