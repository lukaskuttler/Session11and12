#find_3_letter_words("book.txt")

def force_multiple_6():
    """
    Forces multiple of 6 number
    :return: int
    """
    while True:
        num = input("Please give me a multiple of 6: ")
        try:
            num = int(num)
            if num % 6 == 0:
                return num # we are returning the number
            else:
                print("At least you gave me a number.Try again, needs to be multiple of 6")
        except ValueError:
            print("Dont be smart, I need a number")

force_multiple_6()


