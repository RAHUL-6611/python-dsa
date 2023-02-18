
def twosum():
    l =[1,4,2,5,6]
    t=6

    map={}
    for i in range(len(l)):
        if t-l[i] in map:
            k= [i,map[t-l[i]]]
            k.sort()
            return k
        map[l[i]] = i   

print(twosum())    

str1,str2,str3,str4,str5,str6="",""
print(str2)