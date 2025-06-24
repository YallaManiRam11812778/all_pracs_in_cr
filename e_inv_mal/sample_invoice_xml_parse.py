import xml.sax
from xml.sax.xmlreader import AttributesImpl
columns = []
import time

# class InvoiceHandler(xml.sax.ContentHandler):
#     def startElement(self, name: str, attrs:AttributesImpl) -> None:
#         self.current = name
#         return super().startElement(name, attrs)
    
#     def characters(self, content: str) -> None:
#         # if content != "\n":
#         columns.append({self.current:content})
#         return super().characters(content)
    
#     def endElement(self, name: str) -> None:
#         pass
    
# start = time.time()
# parser = xml.sax.make_parser()
# parser.setContentHandler(InvoiceHandler())

# # Parse the XML file
# xml_file = "/home/caratred/Downloads/KULDMFOL241218 .xml"

# # xml_file = "/home/caratred/Documents/ram/test/e_inv_mal/credit_note_sample.xml"
# output = parser.parse(xml_file)
# print(output)
# import polars as pl
# fileptr = open(xml_file,"r")
 
# #read xml content from the file
# xml_content= fileptr.read()
# import xmltodict
# #change xml format to ordered dict
# my_ordered_dict=xmltodict.parse(xml_content)
# pl_df = pl.DataFrame(my_ordered_dict["Invoice"])
# print(pl_df)