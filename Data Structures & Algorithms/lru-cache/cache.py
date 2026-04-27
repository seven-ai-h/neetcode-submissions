# ============================================================
# LRU CACHE — Doubly Linked List + HashMap
# ============================================================
# PATTERN: When you need BOTH O(1) lookup AND O(1) ordering,
# combine a HashMap with a Doubly Linked List.
#
# HashMap alone   → O(1) lookup, but no ordering
# Linked List alone → O(1) insert/remove, but O(n) lookup
# Together        → O(1) everything
#
# WHEN TO RECOGNIZE THIS PATTERN:
# - "Design a cache" problems
# - Any problem needing O(1) access + O(1) eviction
# - Problems tracking "most/least recently used"
# ============================================================


# ============================================================
# NODE CLASS — always define this separately above your main class
# ============================================================
# PATTERN: Doubly linked list nodes need 4 fields:
#   val, key, prev pointer, next pointer
#
# GOTCHA: prev and next always start as None —
# you never pass them as arguments, they get set later
# ============================================================
class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.prev = None  # points to previous node
        self.next = None  # points to next node


# ============================================================
# LRU CACHE CLASS
# ============================================================
class LRUCache:

    # --------------------------------------------------------
    # INIT — always set up dummy head and tail
    # --------------------------------------------------------
    # PATTERN: Dummy nodes eliminate edge cases.
    # Without them, you'd need special logic for empty list,
    # single node, inserting at head, removing at tail, etc.
    #
    # With dummies, the list is NEVER truly empty —
    # head and tail are always there as anchors.
    #
    # Structure:  head <-> [real nodes] <-> tail
    # Most recent is always right after head
    # Least recent is always right before tail
    # --------------------------------------------------------
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}               # key → Node (stores the whole node, not just value!)

        self.head = Node(0, 0)        # dummy head (values don't matter)
        self.tail = Node(0, 0)        # dummy tail (values don't matter)
        self.head.next = self.tail    # connect them to each other
        self.tail.prev = self.head    # empty list: head <-> tail

    # --------------------------------------------------------
    # REMOVE — disconnect a node from the list
    # --------------------------------------------------------
    # PATTERN: To remove node B from ... <-> A <-> B <-> C <-> ...
    #   A.next = C   (node.prev.next = node.next)
    #   C.prev = A   (node.next.prev = node.prev)
    #
    # GOTCHA: Order doesn't matter here since you're reading
    # node.prev and node.next (which don't change), not
    # reassigning them. Just two lines — that's it.
    #
    # GOTCHA: Dummy nodes make this safe even at the edges —
    # you never have to check if A or C is None
    # --------------------------------------------------------
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # --------------------------------------------------------
    # INSERT — always insert right after head (most recent position)
    # --------------------------------------------------------
    # PATTERN: Save references BEFORE changing any pointers.
    # If you change head.next first, you lose track of the old neighbor.
    #
    # To insert B between head and C:
    #   1. Save prev = head, nxt = head.next (C)
    #   2. B.prev = head
    #   3. B.next = C
    #   4. head.next = B
    #   5. C.prev = B
    #
    # GOTCHA: Always 4 pointer changes for a doubly linked list insert
    # --------------------------------------------------------
    def insert(self, node):
        prev = self.head
        nxt = self.head.next    # save BEFORE changing anything!

        node.prev = prev        # B ← head
        node.next = nxt         # B → C
        prev.next = node        # head → B
        nxt.prev = node         # C ← B

    # --------------------------------------------------------
    # GET — return value and mark as most recently used
    # --------------------------------------------------------
    # PATTERN: Any access (get OR put) makes a node "most recent"
    # Always remove + reinsert to move it to the front
    #
    # GOTCHA: Don't forget to move the node — just returning
    # the value without reordering breaks the LRU property
    # --------------------------------------------------------
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1                       # key doesn't exist

        self.remove(self.cache[key])        # remove from current position
        self.insert(self.cache[key])        # reinsert at front (most recent)
        return self.cache[key].val          # return the value

    # --------------------------------------------------------
    # PUT — insert or update, evict LRU if over capacity
    # --------------------------------------------------------
    # PATTERN: Always handle duplicate key first, then new key.
    # For new keys, evict BEFORE inserting (not after).
    #
    # Three cases:
    #   1. Key exists  → update value, move to front
    #   2. Key is new, at capacity → evict LRU, then insert new
    #   3. Key is new, under capacity → just insert new
    #
    # GOTCHA: Save lru = tail.prev BEFORE calling remove(lru).
    # After removal, tail.prev points to a different node!
    #
    # GOTCHA: When evicting, delete from BOTH the linked list
    # AND the cache dictionary — they must always stay in sync
    #
    # GOTCHA: Node(value, key) — match the order in __init__!
    # Node takes val first, then key. Easy to swap accidentally.
    # --------------------------------------------------------
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Case 1: duplicate key — update and move to front
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            # Case 2 & 3: new key
            if len(self.cache) == self.capacity:
                # at capacity — evict least recently used (right before tail)
                lru = self.tail.prev              # save reference first!
                self.remove(lru)                  # remove from linked list
                del self.cache[lru.key]           # remove from dictionary too

            # always insert new node (whether we evicted or not)
            new_node = Node(value, key)           # val first, then key!
            self.cache[key] = new_node            # store in dictionary
            self.insert(new_node)                 # insert at front of list


# ============================================================
# GENERAL PATTERNS TO REMEMBER
# ============================================================
#
# 1. DUMMY HEAD/TAIL
#    Use whenever you have a doubly linked list problem.
#    Eliminates all edge cases for empty list or single node.
#
# 2. SAVE REFERENCES BEFORE MODIFYING POINTERS
#    nxt = self.head.next   ← save first
#    self.head.next = node  ← then modify
#
# 3. HASHMAP + LINKED LIST = O(1) ordered access
#    HashMap stores key → node (the whole node, not just value)
#    Linked list tracks order (head = most recent, tail = least)
#    They ALWAYS stay in sync — update both on every operation
#
# 4. REMOVE + INSERT = MOVE TO FRONT
#    Any time a node is accessed, call remove() then insert()
#    This is how you update LRU ordering in O(1)
#
# 5. EVICT BEFORE INSERT
#    Always check capacity and evict BEFORE adding new node
#    Check == capacity (not >), since you haven't added yet
# ============================================================
