from typing import List
import collections
def nameit(ideas:List[str])->int:
    namemap = collections.defaultdict(set)
    for w in ideas:
        namemap[w[0]].add(w[1:])
    res=0
    for w1 in namemap:
        for w2 in namemap:
            if w1 == w2: 
                continue
            intersect=0
            for t in namemap[w1]:
                if t in namemap[w2]:
                    intersect+=1
            distinct1 = len(namemap[w1])-intersect    
            distinct2 = len(namemap[w2])-intersect    
            res+= distinct1*distinct2

    return res             

ll = ["tofee","cofee","cafe","time"]
print(nameit(ll))    

