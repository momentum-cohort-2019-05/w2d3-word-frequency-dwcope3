import re
f = open("seneca_falls.txt")
wordlist = f.read()

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
 
 
 #lower case all text
wordlist = wordlist.lower()
#remove all punctuation and spacing
wordlist = re.sub(r'[^A-Za-z]', " ", wordlist)
#split words 
wordlist = wordlist.split()
#runs the functions to turn list of words into a dictionary.  then takes the dictionary and sorts it. 


#list for all words not included in STOP_WORDS
remove_stop_words = []

# function which removes stop words from wordlist
# remove_stop_words = [word for word in wordlist if not word in STOP_WORDS]
for word in wordlist:
    if word not in STOP_WORDS:
        remove_stop_words.append(word)

#function to create a new list that counts each word and how many times it is used
word_freq = []
for word in remove_stop_words: 
    word_freq.append(remove_stop_words.count(word))
# print(list(zip(remove_stop_words, word_freq)))

#given a list of words, return a dictionary of word_frequency pairs
def wordlistTofreqdict(remove_stop_words):
    word_freq = [remove_stop_words.count(p) for p in remove_stop_words]
    return dict(zip(remove_stop_words, word_freq))

dictionary = wordlistTofreqdict(remove_stop_words)

#sort dictionary of word_freq in order of descending frequency.
def sortfreqdict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

# dictionary = wordlistTofreqdict(remove_stop_words)
# def get_second_element(seq):
#     return seq[1]
# sorted(dictionary.items(), key=get_second_element, reverse=True)


sorteddictionary = sortfreqdict(dictionary)

#print the sorted pairs in a string from the sorted dictionary
for pair in sorteddictionary: 
    print(str(pair))



# def print_word_freq(file):
#     """Read in `file` and print out the frequency of words in that file."""
#     pass



# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1) 