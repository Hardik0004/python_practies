import json
import pdb
pdb.set_trace()


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":70000 "bonus":8000} } } }"""
isValid = validateJSON(InvalidJsonData)

print("Given JSON string is Valid", isValid)
