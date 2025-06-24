from spacy.matcher import Matcher
from spacy.tokens import Span
import spacy
nlp = spacy.load("en_core_web_sm")
matcher  = Matcher(nlp.vocab)
CHK = [{"LOWER":"chk","POS":"PROPN"},{"POS":"NUM"}]
TBL = [{"LOWER":"tbl","POS":"PROPN"},{"POS":"PROPN"}]
lemma_means_matching_probable_words = [{"LEMMA":"play"}]# takes into consideration as played, playing, plays etc.
text_exact_match_along_with_any_punctuatuion_and_after_punct_any_word_or_anything = [{"TEXT":"CHK"},{"IS_PUNCT":True,"OP":"*"}]
matcher.add("Matched",[CHK,TBL,])
file_path = "/home/caratred/test/NLP/chks_info.txt"
f = open(file_path, "r")
lines = f.readlines()


text_from_nlp = nlp("".join(lines))
matches = matcher(text_from_nlp)

emp = []
# for token in text_from_nlp:
#     print(token.text," : ",token.pos_)
entries = 0
for match_id, start, end in matches:
    if entries == 2:
        entries = 0
    entries +=1
    string_id = nlp.vocab.strings[match_id]
    span = text_from_nlp[start:end]
    print(Span(text_from_nlp,start, end),"$"*100)
    # print(span.text,">>>>>>>>>>>>>>")
