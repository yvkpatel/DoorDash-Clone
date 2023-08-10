import json
from Payment import Payment
#Create dict from json file (unused)
def importfromjson(jsonfile):

    with open(jsonfile, "r") as read_file:
        data = json.load(read_file)
    return data
#Create dict from json string
def importfromjsonstring(jsonstring):
    data = json.loads(jsonstring)
    return data

