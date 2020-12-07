import re
file=open('CommaAi.txt','r')
lines=file.readlines()
arr=[]
for line in lines:
    arr.append(line)

def count(arr):
    print(arr)
    validSet=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    value=arr[4:]
    for i in arr:
        key=i[:3]
        value=i[4:]
        if key in validSet and check(key,value):
            validSet.pop(validSet.index(i[:3]))
    print(validSet)
    if len(validSet)==0:
        return True
    return False

def check(key,value):
    if key=="byr":
        if len(value)!=4:
            return False
        try:
            x=int(value)
        except ValueError:
            return False
        if x>=1920 and x<=2002:
            return True
        return False
    elif key=="iyr":
        if len(value)!=4:
            return False
        try:
            x=int(value)
        except ValueError:
            return False
        if x>=2010 and x<=2020:
            return True
        return False
    elif key=="eyr":
        if len(value)!=4:
            return False
        try:
            x=int(value)
        except ValueError:
            return False
        if x>=2020 and x<=2030:
            return True
        return False
    elif key=="hgt":
        if value[-2:]=="cm":
            if len(value)!=5:
                return False
            try:
                x=int(value[:3])
            except ValueError:
                return False
            if x>=150 and x<=193:
                return True
            return False
        if value[-2:]=="in":
            if len(value)!=4:
                return False
            try:
                x=int(value[:2])
            except ValueError:
                return False
            if x>=59 and x<=76:
                return True
            return False
        return False
    elif key=="hcl":
        if len(value)==7 and value.startswith("#"):
            charset='0123456789abcdef'
            for i in range(len(value)):
                if i==0:
                    continue
                if value[i] not in charset:
                    return False
                continue
            return True
        return False
    elif key=="ecl":
        s={"amb","blu","brn","gry","grn","hzl","oth"}
        if value in s:
            return True
        return False
    elif key=="pid":
        if len(value)==9:
            try:
                x=int(value)
            except ValueError:
                return False
            return True
        return False
l=[]
c=0
for i in arr:
    if not re.search('[a-zA-Z]', i):
        if count(l):
            c+=1
        l=[]
    else:
        tmp=i.split(" ")
        for k in tmp:
            l.append(k.rstrip("\n"))
print(c+1)
