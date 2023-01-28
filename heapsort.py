# Heap and heapsort impl

class HeapSort:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.size = len(arr)
        self.heapify()
    def heapify(self):
        for i in range((self.size-2)//2, -1, -1):
            self.percolate_down(i)
    # max heap
    def percolate_down(self, idx):
        while (2 * idx + 1 <= self.size-1):
            left = 2 * idx + 1
            larger_idx = left
            if left != self.size - 1:
                if self.arr[left+1] > self.arr[left]:
                    larger_idx = left + 1
            if self.arr[idx] < self.arr[larger_idx]:
                self.arr[idx], self.arr[larger_idx] = self.arr[larger_idx], self.arr[idx]
                idx = larger_idx
            else:
                break
    def extract_max(self):
        ret = self.arr[0]
        self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
        self.size -= 1
        self.percolate_down(0)
        return ret
    def percolate_up(self, idx):
        parent = (idx-1) // 2
        while (parent >= 0 and self.arr[parent] < self.arr[idx]):
            # swap
            tmp = self.arr[parent]
            self.arr[parent] = self.arr[idx]
            self.arr[idx] = tmp
            idx = parent
            parent = (parent-1) // 2
    def sort(self):
        for i in range(len(self.arr)-1, -1, -1):
            res = self.extract_max()
            self.arr[i] = res

heap = HeapSort([1,5,2,9,7,0,4,32, 47,4845,15,2,5,86])
# print(heap.arr)
heap.sort()
print(heap.arr)

