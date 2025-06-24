# ner_with_annotationa.py
import spacy
import spacy.displacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json
nlp = spacy.blank("en") # load new spacy model
db = DocBin() # create docbin object

file = open('/home/caratred/test/NLP/annotation_training_data.json')
TRAINING_DATA = json.load(file)

for text, annotation in tqdm(TRAINING_DATA["annotations"]):
    doc = nlp.make_doc(text)
    entities = []
    for start, end, label in annotation["entities"]:
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            entities.append(span)
    doc.ents = entities
    db.add(doc)
db.to_disk("./training_data_spacy.spacy")

# nlp_ner = spacy.load("/home/caratred/test/NLP/model-best")
# doc = nlp_ner("""'Park Hyatt Hyderabad\tPARK HYATT HYDERABAD\tRoad No. 2, Banjara Hills,\tHyderabad, 500034, India\tTel: +91 40 4949 1234\tTAX INVOICE\tFax: +91 40 4949 1235\tRIKA\tTre Forni Resturant\tService charge is optional. In case\tyou wish to revoke it from your bill,\tkindly let your server know.\tFSSAI -10014047000154\tTRE TV FORNI\t4748150 Ashu\tCHK 2823\tTBL 31/1\tGST 3\t13 Mar124 20:43 PM\t'""")
# spacy.displacy.serve(doc, style="ent",port=3000)
# sentence_spans = list(doc.sents)
# print(sentence_spans)
# doc.user_data
