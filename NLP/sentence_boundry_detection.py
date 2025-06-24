import spacy
nlp = spacy.load("en_core_web_sm")
text_by_nlp = nlp("my name is sombary.My lover name is radhika akka aka Tillu-wife")
# for token in text_by_nlp:
#     print(token.text,token.pos_,spacy.explain(token.tag_),token.dep_)
print(len(list(text_by_nlp.sents)))
