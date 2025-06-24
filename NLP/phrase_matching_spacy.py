import spacy
nlp = spacy.load("en_core_web_sm")
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab,attr="LOWER")
file_path = "/home/caratred/test/NLP/chks_info.txt"
f = open(file_path, "r")
lines = f.readlines()
doc = nlp("".join(lines))
phrase_list = ["CHK","TBL"]
pattern = [nlp.make_doc(text) for text in phrase_list]
print(pattern,"^"*100)
matcher.add("phrase",pattern)
matches = matcher(doc)
# print(matcher,">"*100)
for match_id, start, end in matches:
    print(match_id," : ",start," : ",end)
    span = doc[start:end]
    print(span.text,"O"*100)