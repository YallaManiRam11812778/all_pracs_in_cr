import spacy
natural_laguage_process = spacy.load("en_core_web_sm")
text_by_nlp = natural_laguage_process("Rika --- Room service \n Service charge is optional. In case you wish to revoke it from the bill, kindly let your server know.\nFSSAI -001411000154\n 4543454 Baishali\n CHK 4296 TBL 542/1 GSt 1\n 1 Mar'2024 15:50 PM")
from beautifultable import BeautifulTable
TABLE = BeautifulTable()
TABLE.columns.header = ["text","PartsOfSpeech","Explaination Of Tag","DEPendency"]
for token in text_by_nlp:
    TABLE.rows.append([token.text,token.pos_,spacy.explain(token.tag_),token.dep_])
    # print(token.text,"----------------", token.pos_, "+++++++++++++++++++++++++",token.dep_)
print(TABLE)