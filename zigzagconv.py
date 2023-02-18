class Solution:
    def convert(self, s: str, n: int) -> str:
        rowl=["" for i in range(n)]
        if(n==1):
            return s
        i=0
        zz=True
        for k in range(len(s)):
            if (zz and i==n):
                i-=1
                zz = False
            if (not zz and i==0):
               zz=True
               i+=1
            if (zz):
                rowl[i] +=s[k]
                i+=1   
            else:
              i-=1
              rowl[i]+=s[k]

        s=""
        for h in rowl:
            s+= h
        return s        

s = Solution()
print(s.convert("PAYPALISHIRING",3))


