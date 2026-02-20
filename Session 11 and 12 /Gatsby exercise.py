import requests

def download_book(url):
    """
    downloads a book from a url
    :param url: the url for the book
    :return: None
    """
    response = requests.get(url)
    print(response.status_code)
    #save the book
    with open("book.txt", "w") as f:
        f.write(response.text)

#download_book("https://www.gutenberg.org/cache/epub/64317/pg64317.txt")

def find_3_letter_words(book_name):
    """
    find 3 letter words starting with B
    :param book_name: the file containing the book
    :return: None
    """
    unique_words = []
    special_chars = ",.?!;'\n"
    with open(book_name, "r", encoding="utf-8") as f:
        for line in f:
            #remove punctuation
            for c in special_chars:
                line = line.replace(c, "")
            #break down the line into words
            words = line.split(" ")
            for word in words:
                if word not in unique_words and len(word) == 3 and word[0] =="b":
                    unique_words.append(word)
    print(unique_words)

find_3_letter_words("book.txt")