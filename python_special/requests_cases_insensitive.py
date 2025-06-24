from requests.structures import CaseInsensitiveDict
from tkinter import filedialog as fd
data : dict[ str : str | int ] = {
    "name":"Maniram",
    "File":fd.askopenfile()
}
cid : CaseInsensitiveDict[ str | int ] = CaseInsensitiveDict(data)
print(cid["FILE"])
