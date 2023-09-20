# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json

string_json = """
{
    "nome": "Luis",
    "sobrenome": "Henrique",
    "idade": 18,
    "altura": 1.80,
    "endereços": {"casa": "Rua São Pedro, 557, Recanto Verde do Sol"},
    "dinheiro": null
}
"""

person = json.loads(string_json)
person_dump = json.dumps(person, ensure_ascii=False, indent=2)
print(person_dump)
