from collections import Counter

def read_book(name):
    with open(f'./books/{name}.txt') as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_character_occurrences(text):
    return Counter(text.lower())

def report_on_book(book_name, text):
    word_count = count_words(text)
    character_counts = count_character_occurrences(text)

    print(f"=== Begin Report on {book_name} ===")

    # Print word count
    print(f"Contains {word_count} words.")

    # Character counts
    for character in character_counts.most_common():
        if character[0].isalpha():
            print(f"The '{character[0]}' character was found {character[1]} times.")

    print("=== End Report ===")
    

def main():
    book_name = 'frankenstein'
    text = read_book(book_name)
    report_on_book(book_name, text)

main()