# !!! Notice: "pip install Workbook" must be executed before runing the code

#module
import xml.dom.minidom
from openpyxl import Workbook
import numpy as np

#lists of elements
tree = xml.dom.minidom.parse("go_obo.xml") #dom tree
collection = tree.documentElement
terms = collection.getElementsByTagName("term")

workbook = Workbook()
sheet = workbook.active
sheet.append(["id","name","definition","childnodes"])

idmap = {}
cnt = 0
def getid(s):
    global cnt
    if not s in idmap:
        cnt += 1
        idmap[s] = cnt
        return cnt
    return idmap[s]

n = terms.length + 5
edge = 80000
deg = np.full((n), 0)
tot = 0
head = np.full((n), 0)
nxt = np.full((edge), 0)
adj = np.full((edge),0)

# use adjacency list to store edge in the DAG
def add(i, j):
    global tot
    tot += 1
    nxt[tot] = head[i]
    head[i] = tot
    adj[tot] = j

ans = []

#get the information
for term in terms:
    _def = term.getElementsByTagName("def")[0]
    defstr = _def.getElementsByTagName("defstr")[0].childNodes[0].data
    ID = term.getElementsByTagName("id")[0].childNodes[0].data
    if defstr.find("autophagosome") != -1:
        name = term.getElementsByTagName("name")[0].childNodes[0].data
        ans.append((ID,name,defstr))
    child = term.getElementsByTagName("is_a")
    i = getid(ID)
    for node in child:
        j = getid(node.childNodes[0].data)
        add(j, i)
        deg[j] += 1

#print(n, cnt)
#print(edge)

node = {}
def dfs(x):
    if not x in node:
        node[x] = 1
    global cnt
    cnt += 1
    i = head[x]
    while i:
        dfs(adj[i])
        i = nxt[i]

for i in ans:
    cnt = 0
    node.clear()
    dfs(getid(i[0]))
    sheet.append([i[0], i[1], i[2], cnt - 1])

workbook.save("autophagosome.xlsx")
 