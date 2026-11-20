
# supports deletion in heap
class lheap:
    def __init__(self):
        from heapq import heappush, heappop
        self.h = []
        self.valid = {}
    
    def add(self, x):
        self.valid[x] = self.valid.get(x, 0) + 1
        heappush(self.h, x)
    
    def rem(self, x):
        self.valid[x] -= 1
    
    def get(self):
        while self.h and self.valid[self.h[0]] == 0:
            heappop(self.h)
        if self.h:
            return self.h[0]
        return 0
 
 
