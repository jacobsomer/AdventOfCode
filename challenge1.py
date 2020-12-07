def isValid(lower,higher,letter,string):
    left=int(lower)
    right=int(higher)
    if string[left-1]==letter and string[right-1]==letter:
        return False
    if string[left-1]!=letter and string[right-1]!=letter:
        return False
    return True

file=open('CommaAi.txt','r')
lines=file.readlines()
arr=[]
for line in lines:
    arr.append(line)

total=0
for i in arr:
    l=""
    h=""
    letter=""
    string=""
    dash=False
    colon=False
    space=False
    for k in i:
        if k=="-":
            dash=True
        if k==" ":
            space=True
        if k==":":
            colon=True
        if not dash:
            l=l+k
        if dash and not space and k!="-":
            h=h+k
        if space and not colon:
            letter=k
        elif dash and space and colon and k!=":" and k!=" ":
            string+=k
    if isValid(l,h,letter,string):
        total+=1
print(total)
