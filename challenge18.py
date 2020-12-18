# 2 * 3 + (4 * 5) becomes 26.
# 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.

def getLevels(arr):
    m=0
    tmp=[]
    level=0
    for i in range(len(arr)):
        if arr[i]==")":
            level-=1
        elif arr[i] == "(":
            level+=1
            if m<level:
                m=level
                tmp=[i]
            elif m==level:
                tmp.append(i)

    return tmp



def parse(line):
    arr=[]
    for i in line:
        arr.append(i)
    for j in range(len(arr)):
        try:
            if arr[j]==" ":

                    arr.pop(j)
        except IndexError:
            pass
    return arr


def simplify(arr,start):
    if len(arr)==1:
        return arr
    for j in range(len(start)):
        k=start[j]
        while k<len(arr):

            try:
                if arr[k]==')':
                    break
                if arr[k].isnumeric() and arr[k+2].isnumeric():
                    if arr[k+1]=="+":
                        arr[k+1]=str(int(arr[k])+int(arr[k+2]))
                        arr.pop(k)
                        arr.pop(k+1)
                        for i in range(j+1,len(start)):
                             start[i]-=2
                    elif arr[k+1]=="*":
                        k+=1
                else:
                    k+=1

            except IndexError:
                    k+=1
    return arr,start

def simplfy2(arr,start):
    if len(arr)==1:
        return arr
    for j in range(len(start)):
        k=start[j]
        while k<len(arr):
            try:
                if arr[k]==')':
                    break
                if arr[k].isnumeric() and arr[k+2].isnumeric():
                    if arr[k+1]=="*":
                        arr[k+1]=str(int(arr[k])*int(arr[k+2]))
                        arr.pop(k)
                        arr.pop(k+1)
                        for i in range(j+1,len(start)):
                             start[i]-=2
                    if arr[k+1]=='+':
                        k+=1
                else:
                    k+=1

            except IndexError:
                    k+=1
    return arr,start


def removeLevels(arr,locs):
    for i in locs:
        arr.pop(i)
        arr.pop(i+1)
        for k in range(len(locs)):
            locs[k]-=2

    return arr


def solve(arr):
    i=0
    while i< 4 and len(arr)>1:

        tmp=getLevels(arr)
        if len(tmp)==0:
            break
        arr=simplify(arr,tmp)

        arr=simplfy2(list(arr[0]),list(arr[1]))

        arr=removeLevels(list(arr[0]),list(arr[1]))

    arr=simplify(arr,[0])
    return int(list(simplfy2(list(arr[0]),list(arr[1])))[0][0])


def final(arr):
    arr=str(arr)
    started=False
    notFinished=True
    final=''
    for i in arr:
        if not i.isnumeric() and started==True:
            break
        if i.isnumeric() and not started:
            started=True
        if started and i.isnumeric():
            final+=i
    return int(final)





file=open('CommaAi.txt','r')
lines=file.readlines()
arr=[]
for line in lines:
    arr.append(line)

total=0
for i in arr:
    total+=(solve(parse(i)))
print(total)


#final answer: 218621700997826
