from functools import reduce
import json 

raw = open("aquarium.json", encoding="utf8")
data = json.load(raw)
marinhos = data['data']


