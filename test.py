import re
f = open("seneca_falls.txt")
all_text = (f.read())

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
 
 #lower case all text
all_text = all_text.lower()
#remove all punctuation and spacing
all_text = re.sub(r'[^A-Za-z]', " ", all_text)
#split words 
splitter = all_text.split()

# test case