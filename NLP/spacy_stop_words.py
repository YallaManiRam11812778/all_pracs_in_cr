import spacy
import spacy.lang
import spacy.lang.en
nlp = spacy.load("en_core_web_sm")
nlp_text = nlp("Rika --- Room service \n Service charge is optional. In case you wish to revoke it from the bill, kindly let your server know.\nFSSAI -001411000154\n 4543454 Baishali\n CHK 4296 TBL 542/1 GSt 1\n 1 Date-   Mar'2024 15:50 PM")
stopwords = spacy.lang.en.stop_words.STOP_WORDS
# print(stopwords)

# # Lemmatization and Stop_words
# for token in nlp_text:
#     if token.text in stopwords:
#         print(token.text, token.lemma_)

# Word Freq counter
from collections import Counter
word_freq = Counter(str(nlp_text).split())
print(word_freq,"\n","^"*100,"\n\n")
words = [token.text for token in nlp_text if not token.is_stop and not token.is_punct]
# print(words,"UY"*100)
# combined = " ".join(words)
word_freq = Counter(words)
print(word_freq)