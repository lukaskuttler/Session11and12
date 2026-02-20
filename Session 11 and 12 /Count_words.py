# top 5 list: 1. the 2. a 3. if  4. and 5.of

def count_unique_words(filename):
    word_dict = {}
    special_chars = ".,';?!\n"
    with open(filename) as f:
        for line in f:
            line = line.lower() #the is the same as the
            for c in special_chars: #remove special chars
                line = line.replace(c, "") #remove special characaters
            words = line.split(" ") #extract words
            for word in words:
                if len(word) == 0:
                    continue
                if word not in word_dict: # if its the first time, I add it
                    word_dict[word] = 1
                else: # otherwise I increse the counter again
                    word_dict[word] = word_dict[word] + 1
    return word_dict

def get_most_frequent_words(word_dict):
    common_words = []
    frequencies = list(word_dict.values())
    frequencies.sort(reverse=True)
    frequencies = frequencies[:10] #just care about the 10 most common
    for freq in frequencies:
        for key, value in word_dict.items():
            if freq == value:
                common_words.append(f"{key}: {value}")
                #word_dict.pop(key)
    return common_words

print(count_unique_words("book.txt"))
print("Unique words in great Gatsby:", len(count_unique_words("book.txt")))
unique_words = count_unique_words("book.txt")
print(get_most_frequent_words(unique_words))