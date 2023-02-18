

def gcd(str1,str2):
    ls1,ls2 = len(str1),len(str2)
    
    def isDivisible(l):
        if ls1%l or ls2%l:
            return False
        f1,f2 = int(ls1/l),int(ls2/l)
        return str1[:l]*f1 == str1 and str2[:l]*f2 == str2  

    for l in range(min(ls1,ls2),0,-1):
        if isDivisible(l):
            # print("Divisible")
            return  str1[:l]
    return ""

print(gcd("ABC","ABCABC"))    