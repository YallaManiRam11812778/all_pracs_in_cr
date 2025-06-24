from tinydb import TinyDB
from tinydb import Query
db = TinyDB("/home/caratred/Documents/ram/test/e_inv_mal/sample_json_parse.json")
# Todo = Query()
# print(len(db))
# searched = db.search(Todo.Invoice)
# print(searched)
print(db.all())