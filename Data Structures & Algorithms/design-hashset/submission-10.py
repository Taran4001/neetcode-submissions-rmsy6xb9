class MyHashSet:

    def __init__(self):
        self.hasSet = [False] * 1000001

    def add(self, key: int) -> None:
        self.hasSet[key] = True
        return None

    def remove(self, key: int) -> None:
        self.hasSet[key] = False
        return None
    
    def contains(self, key: int) -> bool:
        return self.hasSet[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)   