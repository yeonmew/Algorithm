class MaxHeap(object):
 
    def __init__(self):
        self.queue = []
 
    def insert(self, n):
        # 맨 마지막에 삽입할 원소를 임시로 추가한다.
        self.queue.append(n)
        last = len(self.queue) - 1
        # 부모와 크기를 비교하여 바꾼다.
        while 0 <= last:
            parent = self.parent(last)
            if 0 <= parent and self.queue[parent] < self.queue[last]:
                self.swap(last, parent)
                last = parent
            else:
                break
 
    def delete(self):
        last = len(self.queue) -1
        if last < 0:
            return -1
        self.swap(0, last)
        max = self.queue.pop()
        self.maxHeapify(0) # root에서부터 자식들과 값을 비교하여 바꾼다.
        print(max)
        return max
 
 
    # 임시 root값부터 자식들과 값을 비교하여 바꾼다. 
    def maxHeapify(self, i):
        left = self.leftchild(i)
        right = self.rightchild(i)
        max = i # 큰 값의 index를 넣는다.
 
        if left <= len(self.queue) -1 and self.queue[max] < self.queue[left]:
            max = left
        if right <= len(self.queue) -1 and self.queue[max] < self.queue[right]:
            max = right
 
        # 가장 큰게 아니면 바꾼다.
        if max != i:
            self.swap(i, max)
            self.maxHeapify(max)
 
 
    def swap(self, i, parent):
        self.queue[i], self.queue[parent] = self.queue[parent], self.queue[i]
 
 
    def parent(self, index):
        return (index -1) // 2
 
 
    def leftchild(self, index):
        return index*2 + 1
 
 
    def rightchild(self, index):
        return index*2 + 2
 
 
    def printHeap(self):
        print(self.queue)