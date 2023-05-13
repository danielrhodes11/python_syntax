def print_upper_words(words, letters):
    """ prints out uppercase word on seperate line """
    for word in words:
        if word[0].lower() in letters:
            print(word.upper())
