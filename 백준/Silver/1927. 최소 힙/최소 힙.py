import sys


class Heap():
    def __init__(self):
        self.heap = [0]*100000
        self.heap_cnt = 0

    def add(self, val):
        pivot = self.heap_cnt
        self.heap[self.heap_cnt] = val
        self.heap_cnt += 1
        while pivot > 0:
            ppivot = pivot
            pivot -= 1
            pivot = pivot >> 1
            if self.heap[pivot] > val:
                self.heap[ppivot] = self.heap[pivot]
                self.heap[pivot] = val
            else:
                return
        return

    def pop(self):
        if self.heap_cnt == 0:
            return 0
        val = self.heap[0]

        self.heap_cnt -= 1
        self.heap[0] = self.heap[self.heap_cnt]
        pivot = 0
        while True:
            ppivot = pivot
            pivot = pivot << 1
            pivot += 1
            if pivot >= self.heap_cnt:
                break
            elif pivot + 1 == self.heap_cnt:
                if self.heap[ppivot] < self.heap[pivot]:
                    break
                tmp = self.heap[ppivot]
                self.heap[ppivot] = self.heap[pivot]
                self.heap[pivot] = tmp
                break
            else:
                if self.heap[pivot] > self.heap[pivot+1]:
                    pivot += 1
                if self.heap[ppivot] < self.heap[pivot]:
                    break
                tmp = self.heap[pivot]
                self.heap[pivot] = self.heap[ppivot]
                self.heap[ppivot] = tmp

        return val


myheap = Heap()

n = int(sys.stdin.readline().strip())
for _ in range(n):
    inp = int(sys.stdin.readline().strip())
    if inp == 0:
        print(myheap.pop())
    else:
        myheap.add(inp)
        
