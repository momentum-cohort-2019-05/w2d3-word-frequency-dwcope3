import re
f = open("seneca_falls.txt")
wordlist = f.read()

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

wordlist = wordlist.lower()
wordlist = re.sub(r'[^A-Za-z]', " ", wordlist)
wordlist = wordlist.split()

di = dict()
clean_wordlist = []
#cleans stop words out of wordlist
for w in wordlist:
    if w not in STOP_WORDS:
        clean_wordlist.append(w)

for w in clean_wordlist:
    di[w] = di.get(w,0) + 1
#alternate way to say same thing
    # if w in di:
    #     di[w] = di[w] + 1
    # else:
    #     di[w] = 1

# print(di)

for k,v in sorted(di.items(), key = lambda item:item[-1], reverse=True):
    # print ('{:*len(v)}'.format(k, "|", v))
    print(k, "|", v)


# print(di)

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