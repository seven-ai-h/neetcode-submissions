# LRU Cache — Doubly Linked List + HashMap
#
# Key insight: combine two structures since neither works alone
#   HashMap        → O(1) lookup but no ordering
#   Doubly Linked  → O(1) insert/remove but O(n) lookup
#   Together       → O(1) everything
#
# Most recent node lives right after head
# Least recent node lives right before tail


class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key → whole Node object, not just value

        # Dummy nodes eliminate edge cases at the head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        # Disconnect node from its neighbors — always just 2 lines
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        # Always insert right after head (most recent position)
        # Save references BEFORE changing any pointers
        prev = self.head
        nxt = self.head.next
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move to front — any access makes it most recently used
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to front
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            if len(self.cache) == self.capacity:
                # Evict LRU — save reference before removing!
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]  # sync both structures

            # Note: Node takes val first, then key — don't swap!
            new_node = Node(value, key)
            self.cache[key] = new_node
            self.insert(new_node)


# Patterns to study next:
#
# 1. Doubly Linked List
#    Practice insert and remove until you can write them from memory.
#    The 4-pointer insert and 2-pointer remove show up in many problems.
#
# 2. HashMap + Data Structure combos
#    LRU pairs HashMap with Linked List. You'll see similar combos
#    with HashMap + Heap (e.g. task scheduler) or HashMap + Stack.
#    The pattern is always: one structure for lookup, one for ordering.
#
# 3. Dummy/Sentinel nodes
#    Anytime you use a linked list, default to dummy head and tail.
#    Saves you from writing special case logic for empty or single node lists.
#
# 4. Two pointer technique
#    Related to linked lists — fast/slow pointers for cycle detection,
#    finding middle of list, nth node from end.
#
# 5. Monotonic Stack/Queue
#    Next step up in complexity from this problem. Used when you need
#    O(1) access to the min/max of a sliding window.
