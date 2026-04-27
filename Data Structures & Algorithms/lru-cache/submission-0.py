class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def insert(self, node):
        prev = self.head
        nxt = self.head.next
        node.prev = prev
        prev.next = node
        node.next = nxt
        nxt.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                if lru != self.head:
                    self.remove(lru)
                    del self.cache[lru.key]
            
            new_node = Node(value, key)
            self.cache[key] = new_node
            self.insert(new_node)




