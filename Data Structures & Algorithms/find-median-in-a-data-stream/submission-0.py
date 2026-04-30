# Find Median From Data Stream — Two Heaps
#
# Key insight: split numbers into two halves.
# You only ever need the TOP of each half to find the median —
# no sorting needed, no scanning the whole list.
#
# left  = max heap → holds the smaller half, top is the largest of them
# right = min heap → holds the larger half, top is the smallest of them
#
# Visual:
#   left:  [2, 1]  right: [3, 5]
#              ↑              ↑
#          max of left    min of right
#   median = (2 + 3) / 2 = 2.5


from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.left = []   # max heap (smaller half)
        self.right = []  # min heap (larger half)

    def addNum(self, num: int) -> None:
        # always push to left first
        # negate because Python only has min heap —
        # negating tricks it into behaving like a max heap
        heappush(self.left, -num)

        # boundary check — every number in left must be <= every number in right
        # if top of left is greater than top of right, they're in the wrong heap
        # guard with "self.right and" to avoid comparing when right is empty
        if self.right and -self.left[0] > self.right[0]:
            val = heappop(self.left)       # pop max from left (still negated)
            heappush(self.right, -val)     # push to right (negate back to positive)
            val = heappop(self.right)      # pop min from right
            heappush(self.left, -val)      # push to left (negate to store)

        # balance check — left can have at most 1 more element than right
        # if left gets too big, move its top to right
        if len(self.left) > len(self.right) + 1:
            val = heappop(self.left)       # pop max from left (negated)
            heappush(self.right, -val)     # push to right (negate back)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            # even total — average the two tops
            # negate left[0] because it was stored negated
            return float(-self.left[0] + self.right[0]) / 2
        else:
            # odd total — left always has the extra element
            # return top of left, negated back to actual value
            return -self.left[0]


# Negation trick — the most confusing part
#
# Python's heapq is ALWAYS a min heap — smallest value goes to top.
# There is no max heap built in.
#
# To fake a max heap, negate every value going in and negate again coming out:
#   push:  heappush(heap, -num)    → stores -5 instead of 5
#   peek:  -heap[0]                → negates -5 back to 5
#   pop:   val = heappop(heap)     → val is -5
#          -val                    → gives you 5 back
#
# The heap still thinks it's doing min heap — it just doesn't know
# that your "smallest negative" is actually your "largest positive"


# Two Heap Pattern — use when you need the median of a stream
#
# The pattern always looks like:
#   left  = max heap (smaller half) — negate values
#   right = min heap (larger half)  — normal values
#
# Two invariants to maintain after every addNum:
#   1. boundary: max of left <= min of right
#   2. balance:  len(left) can exceed len(right) by at most 1
#
# findMedian is then just:
#   even total → (top of left + top of right) / 2
#   odd total  → top of left


# Patterns to study next:
#
# 1. Sliding window median
#    Same two heap idea but you also remove numbers as the window moves.
#    Harder because heaps don't support arbitrary removal efficiently.
#
# 2. K closest points to origin
#    Use a max heap of size k — if heap exceeds k, pop the largest.
#    Same negation trick applies.
#
# 3. Kth largest element in a stream
#    Min heap of size k — top of heap is always the kth largest.
#    Very common interview problem, builds directly on this.
#
# 4. Merge k sorted lists
#    Push the first element of each list into a min heap.
#    Pop the smallest, push the next element from that list.
#
# 5. Dijkstra's algorithm
#    BFS but with a min heap instead of a queue.
#    Always process the shortest known distance next.
