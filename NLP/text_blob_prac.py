from textblob import TextBlob
print("?????????????????????")
# import nltk
# nltk.download('punkt')
wiki = TextBlob("""Kalam was elected as the 11th president of India in 2002 with the support of both the ruling Bharatiya Janata Party and the then-opposition Indian National Congress. Widely referred to as the "People's President",[6] he returned to his civilian life of education, writing and public service after a single term. He was a recipient of several prestigious awards, including the Bharat Ratna, India's highest civilian honour.""")
print(wiki.noun_phrases)

testimonial = TextBlob("The beer is best.But the hangover is not good.")
print(testimonial.pos_tags)
print(testimonial.sentiment.polarity)


from textblob import Blobber
from textblob.taggers import NLTKTagger
tb = Blobber(pos_tagger=NLTKTagger())
print("&"*100)
blob1 = tb("This is a maniram. My mother is gita")
blob2 = tb("This is not YM rao.")
print(blob1.pos_tagger is blob2.pos_tagger,"+"*100)