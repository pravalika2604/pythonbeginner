res = []
cs = ch =sw= 0

def heapsort(heap):
    global res,cs
    cs+=1
    if len(heap)>1:
        n = (len(heap)//2)-1
        for i in range(n,-1,-1):
            heapify(heap,i)
        res.append(heap[0])
        heap[0] = heap[len(heap)-1]
        heap.pop()
        heapsort(heap)
    else:
        res.append(heap[0])

def heapify(heap,i):
    global ch,sw
    ch+=1
    small = i
    l = 2*i+1
    r = 2*i+2
    if l<len(heap) and heap[l]<heap[small]:
        small = l
        sw=sw+1
    if r<len(heap) and heap[r]<heap[small]:
        small = r
        sw=sw+1
    swap = heap[i]
    heap[i] = heap[small]
    heap[small] = swap

    if small!=i:
        heapify(heap,small)

print("Enter the array:")
arr = [int(x) for x in input().split()]
heapsort(arr)
print("The sorted array is :")
print(res)
print("Heapify called {} times and Heapsort called {} times,".format(ch,cs))