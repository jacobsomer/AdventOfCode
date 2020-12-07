
file=open('CommaAi.txt','r')
lines=file.readlines()
arr=[]
for line in lines:
    arr.append(line)
def path(right,down):
    r=right
    d=down
    down=down
    right=right
    count=0
    while down<len(arr):
        if arr[down][right]=='#':
            count+=1
        down+=d
        right=(right+r)
        right=right%(len(arr[0])-1)
    return count
print(path(1,1)*path(3,1)*path(5,1)*path(7,1)*path(1,2))
print(path(3,1))
