from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
    def addNum(self, num: int) -> None:
        heappush(self.left, -num) #puts the numbers in order
        if self.right and -self.left[0] > self.right[0]:
            val = heappop(self.left)
            heappush(self.right, -val)
            val = heappop(self.right)
            heappush(self.left, -val)

        if len(self.left) > len(self.right) + 1:
            val = heappop(self.left) 
            heappush(self.right, -val)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return float(-self.left[0] + self.right[0])/2
        else:
            if len(self.left) > len(self.right):
                return -self.left[0]
            else:
                return self.right[0]
        