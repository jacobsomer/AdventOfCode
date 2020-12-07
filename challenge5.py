import itertools
file=open('CommaAi.txt','r')
lines=file.readlines()
arr=[]
for line in lines:
    arr.append(line)

def split(arr,val):
    left=[]
    right=[]
    for i in range(0,int(len(arr)/2)):
        left.append(arr[i])
    for k in range(int(len(arr)/2),len(arr)):
        right.append(arr[k])
    if val=="R"or val=="B":
        return right
    if val=="L" or val=="F":
        return left

max=0
final=[]
for i in arr:
    i=i[:10]
    row=i[:7]
    col=i[-3:]
    rowarr=[int(x) for x in range(0,128)]
    colarr=[int(x) for x in range(0,8)]
    for j in row:
        rowarr=split(rowarr,j)
    for k in col:
        colarr=split(colarr,k)
    if (rowarr[0]*8+colarr[0])>max:
        max=rowarr[0]*8+colarr[0]
    if (rowarr[0]*8+colarr[0]==813):
        print(i,rowarr[0],colarr[0])
    final.append(rowarr[0]*8+colarr[0])

def findID(allSeatsArr):
    mockIds=set()
    for j in range(12,112):
        for k in range(0,8):
            id=j*8+k
            # print(id," ",j)
            mockIds.add(id)
    for i in allSeatsArr:
        if i==813:
            print("H")
        mockIds.remove(i)
    return mockIds
s=findID(final)
print(s)
print(max)
