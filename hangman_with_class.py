import random

class FileAction ():
    #def __init__ (self, filenname):
        #self.filename = filename
        #return None

    def _loadwords (filename):
        wordfile = open(filename, 'r')
        content = wordfile.read()
        wordlist = content.split()
        return wordlist

    @classmethod
    def pick_random_word(self, filename):
        word = random.choice(self._loadwords(filename))
        return word

