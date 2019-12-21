def check_pal(word):
    word = word.casefold()
    rev_word = reversed(word)
    
    if list(word) == list(rev_word):
        print("The word is a Palindrome.")
    else:
        print("The word is not a Palindrome.")

gword = str(input("Write a word to Check whether the word is Palindrome or not: "))
check_pal(gword)