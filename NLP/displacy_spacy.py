import spacy
from spacy import displacy
natural_laguage_process = spacy.load("en_core_web_sm")
text_by_nlp = natural_laguage_process("Rika --- Room service \n Service charge is optional. In case you wish to revoke it from the bill, kindly let your server know.\nFSSAI -001411000154\n 4543454 Baishali\n CHK 4296 TBL 542/1 GSt 1\n 1 Date-   Mar'2024 15:50 PM")
print(text_by_nlp,">"*100)
displacy.serve(text_by_nlp,style="dep",port=3000,options={"distance":90,"compact":True})