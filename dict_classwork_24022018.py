#Dictionary
FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print ("Loading word list from file...)"
    # inFile: file
    inFile = open(FILENAME, 'r')
    # line: string
    line = inFile.read()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist

list_of_words = load_words()
#print (list_of_words)

def generate_dict (wordlist):
    word_dict = {}
    for word in wordlist:
        word_dict[word] = len(word)
    return word_dict

#print (generate_dict(list_of_words))



def dict_group(wordlist):
    word_group_dict = {}
    for word in wordlist:
        word_key = str(len(word)) + "letters"
        if word_key in word_group_dict.keys():
            word_group_dict[word_key].append(word)

        else:
            new_list = [word]
            word_group_dict[word_key] = new_list

    return word_group_dict

print (dict_group(list_of_words)['3letters'])

print (dict_group(list_of_words)['2letters'])

print (dict_group(list_of_words)['8letters'])
exit()
