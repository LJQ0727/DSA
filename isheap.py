class IsHeap:
    def isminheap(self, arr, start, stop):
        # compare the start with its children
        if 2 * start + 1 > len(arr) - 1:
            return True
        minidx = 2 * start + 1
        if minidx+1 <= len(arr) - 1:
            # caution: '>' not '<'
            if arr[minidx] > arr[minidx+1]:
                minidx = minidx + 1
            return arr[start] < arr[minidx] and self.isminheap(arr, 2 * start + 1, stop) \
                and self.isminheap(arr, 2 * start + 2, stop)
        else:
            return arr[start] < arr[minidx] and self.isminheap(arr, 2 * start + 1, stop)
        
heap = IsHeap()
inp = [90, 15, 10, 11, 8, 4, 7, 3]
inp.reverse()
print(inp)
print(heap.isminheap(inp, 0, len(inp)-1))
