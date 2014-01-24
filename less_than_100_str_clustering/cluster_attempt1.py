import nltk
import string, re
from nltk.corpus import stopwords

sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
string_map_table = string.maketrans("","")
data = re.sub("\d","", open("../data.txt").read().replace("\n"," ").lower())
sentences = sentence_detector.tokenize(data.strip())

cleansed = []
for s in sentences:
	s=s.translate(string_map_table, string.punctuation)
	cleansed.append(sorted(list(set([x for x in s.split() if x not in stopwords.words("english")]))))

print sentences
print cleansed
