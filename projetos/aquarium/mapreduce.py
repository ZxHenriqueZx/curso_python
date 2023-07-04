from functools import reduce
import json 

raw = open("aquarium.json", encoding="utf8")
data = json.load(raw)
marinhos = data['data']

def type_marinhos(marinho):
    return marinho['type'], 1

def reducer(acc, val):
    #print(val)
    if val[0] not in acc.keys():
        acc[val[0]] = 0 + val[1]
    else:
        acc[val[0]] = acc[val[0]] + val[1]
    #print(acc)    
    return acc
list_type = [type_marinhos(marinho) for marinho in marinhos]

times_type = reduce(reducer, list_type, {})

for ty, num in times_type.items():
    print(f'{ty} apareceu {num} vezes')

