import json
import heapq


with open('me.json',encoding="utf8") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

Dict = {}

counts = dict()
for i in jsonObject['metamask']['permissionsHistory']:
  counts[i] = counts.get(i, 0) + 1

with open('pikumobile.txt',encoding="utf8") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

for i in jsonObject['metamask']['permissionsHistory']:
  counts[i] = counts.get(i, 0) + 1



result = {k: v for k, v in counts.items() if v>=2}
s = json.dumps(result)
with open('results.txt', 'w') as f:
    f.write(s)
# print(counts)
# print(heapq.nlargest(10, counts, key=counts.get))