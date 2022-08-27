import json
dict1={"name":"amara vathi",
       "age":38,
       "topic":"pyton"
       }
string=json.dumps(dict1)
print(string)
print(type(string))
