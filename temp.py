import json

f = open('example.json')

data = json.load(f)

print(data["analyzedInstructions"][0]["steps"][0]["step"])

for i in range(len(data["analyzedInstructions"][0]["steps"])):
    print(f"steps {i+1} ", data["analyzedInstructions"][0]["steps"][i]["step"])