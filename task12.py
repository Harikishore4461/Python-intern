import json
#dictionary
print(json.dumps({"Name":"john","doe":20}))
#list
print(json.dumps(["Amala","Dany"]))
#string
print(json.dumps(("Carolina","Matt")))
#tuple
print(json.dumps("Elena"))
#integer
print(json.dumps(80))
#float
print(json.dumps(25.1))
#True
print(json.dumps(True))
#False
print(json.dumps(False))
#None
print(json.dumps(None))