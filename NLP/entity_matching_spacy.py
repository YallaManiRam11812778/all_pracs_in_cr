import spacy
from spacy.pipeline import EntityRuler
from spacy.lang.en import English


file_path = "/home/caratred/test/NLP/chks_info.txt"
f = open(file_path, "r")
lines = f.readlines()
# for token in 
nlp = English()
ruler = nlp.add_pipe("entity_ruler")
nlp = spacy.load("en_core_web_sm")
text_from_nlp = nlp("".join(lines))
for ent in text_from_nlp.ents:
    print(ent.text,ent.label_)
print(spacy.explain("WORK_OF_ART"))# GPE, FAC, WORK_OF_ART, DATE, ORG, CARDINAL, TIME, PERSON

# patterns = [{"label":"ORG","pattern":[{"lower":"chk"},{"ORTH":str(i)}]} for i in range(10000)]
# # print(patterns)
# # with nlp.select_pipes(enable="tagger"):
# ruler.add_patterns(patterns)
# doc = nlp("".join(lines))
#     # print()
# # print(doc)

# for ent in doc.ents:
#     print(ent.text)