import operator
import itertools
d = [{"name":"tobi","class":"1","age":"14", "gender":"m"},{"name":"joke","class":"1","age":"18", "gender":"f"}, {"name":"mary","class":"2","age":"14", "gender":"f"},{"name":"kano","class":"2","age":"15", "gender":"m"},{"name":"ada","class":"1","age":"15", "gender":"f"},{"name":"bola","class":"2","age":"10", "gender":"f"},{"name":"nnamdi","class":"1","age":"15", "gender":"m"}]
d = sorted(d, key=operator.itemgetter("class","age"))
outputList=[]
for i,g in itertools.groupby(d, key=operator.itemgetter("class","age")):
     outputList.append(list(g))
print(outputList,"?"*100)