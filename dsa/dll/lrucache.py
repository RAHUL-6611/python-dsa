

class LRUCache: 
  
    # initializing capacity 
    def __init__(self, capacity): 
        self.cache = {} 
        self.capacity = capacity 
        self.lru_list = [] 

    # get item from cache  
    def get(self, key): 

        # if key is present in cache  
        if key in self.cache: 

            # move the key to the end of lru_list  
            self.lru_list.remove(key) 
            self.lru_list.append(key) 

            return self.cache[key] 

        return -1

    # set item in cache  
    def set(self, key, value): 

        # if key is not present in cache  
        if key not in self.cache.keys() and len(self.cache) == self.capacity: 

            # remove least recently used element  
            lru_element = self.lru_list[0] 
            del self.cache[lru_element] 

            # remove lru element from lru list  
            del self.lru_list[0] 

        elif key in self.cache.keys(): 

            # move the existing key to the end of lru list  
            self.lru_list.remove(key)             

        # set new value in cache and add it to lru list     
        self.cache[key] = value     
        self.lru_list.append(key)


# if __name__ == "__main__":
m = LRUCache(0)
op = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
val =[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]        

for x in range(len(op)):
    if op[x] == "LRUCache": 
        m.capacity = op[x]
    elif op[x] == "put":
        m.set(val[x][0],val[x][1])
    elif op[x] == "get":
        print(m.get(val[x][0]))


# print(m.lru_list)                