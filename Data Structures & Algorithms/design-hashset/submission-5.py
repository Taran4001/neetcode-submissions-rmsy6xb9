class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class MyHashSet:

    def __init__(self):
        self.hashSet = [Node(0) for _ in range(10001)]

    def add(self, key: int) -> None:
        index = key % len(self.hashSet)
        curr = self.hashSet[index]
        while curr.next:
            if curr.next.data == key:
                return
            curr = curr.next
        curr.next = Node(key)
        return

    def remove(self, key: int) -> None:
        index = key % len(self.hashSet)
        curr = self.hashSet[index]
        while curr.next:
            if curr.next.data == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        return

    def contains(self, key: int) -> bool:
        index = key % len(self.hashSet)
        curr = self.hashSet[index]
        while curr.next:
            if curr.next.data == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)