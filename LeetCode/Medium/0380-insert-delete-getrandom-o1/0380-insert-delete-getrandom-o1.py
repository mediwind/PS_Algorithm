import random


class RandomizedSet:
    def __init__(self):
        self.dict = dict()
        self.list = list()
    
    
    def insert(self, val: int) -> bool:
        if val in self.dict.keys():
            return False
        else:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
    
    
    def remove(self, val: int) -> bool:
        if val in self.dict.keys():
            last, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last] = last, idx
            self.list.pop()
            del self.dict[val]
            return True
        else:
            return False

        
    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()