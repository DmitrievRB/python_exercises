import json

with open("visit.json", encoding="utf8") as myFile:
    strfile = myFile.read()
    template = json.loads(strfile)
print(template)
print(type(template))
