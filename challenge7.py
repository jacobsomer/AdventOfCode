file=open('CommaAi.txt','r')
lines=file.readlines()
arr=[]
for line in lines:
    arr.append(line)
dictionairy={}
# format {'bagname':[[1,'othertype'],[2,'secondtype'],...}
for k in arr:
    k=k.split()
    v=[]
    key=""
    tmp=""
    val=None
    vals=False
    count=0
    br=False
    for i in range(len(k)):
        if k[i]=="no":
            dictionairy[key]=[[0,"No"]]
            br=True
            break
        if k[i]=="contain":
            vals=True
        if not vals:
            key+=k[i].rstrip("s,.bag")
        elif k[i]!="contain":
            if count==0:
                val=int(k[i])
                count+=1
            elif count<3:
                tmp+=k[i].rstrip(",.bags")
                count+=1
            else:
                tmp+=k[i].rstrip(",.sbag")
                tup=[val,tmp]
                v.append(tup)
                tmp=""
                val=None
                count=0
    if not br:
        dictionairy[key]=v


final=0
def dfs(graph, node, visited,level):
    global final
    if node=="No":
        return
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            final+=n[0]*level
            dfs(graph,n[1], visited,level+n[0])
    return visited

def visit(dictionairy):
    count=0
    print(len(dictionairy))
    visited=[]
    dfs(dictionairy,"shinygold",visited,1)
    if "shinygold" in visited:
        count+=1
    for i in visited:
        print(i,dictionairy[i])
    return count
visit(dictionairy)

print(final)
