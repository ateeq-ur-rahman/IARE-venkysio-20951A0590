'''
Heap Sort Algorithm
 Haapsort(A)
 Build-MaxHeap(A)
 for i=A.length downto 2
 exchange A[i] with A[1]
A.heap-Size=A.heap-Size-1
Max-Heapify(A,1)
Build-Maxheap------Algo
A.heapsize=A.length
for i=A.length/2 downto 1
Max-heapify(A,i)
Max-Heapify ------Algo 
l=left(i)
r=right(i)
if(l<=A.heapsize and A[l]>A[i])
lar=l
else:
lar=i
if r<=A.heap-size and A[r]>A[lar]
lar=r
if lar!=i
exchage A[i] with A[lar]
Max-HEapify(A,lar)
--The Above description is just a algorithm of heapsort

'''

def heapify(arr, n, i):
    larg = i  
    l = 2 * i + 1  
    r = 2 * i + 2 
    if l < n and arr[i] < arr[l]:
        larg = l
    if r < n and arr[larg] < arr[r]:
        larg = r
    if larg != i:
        (arr[i], arr[larg]) = (arr[larg], arr[i])
        heapify(arr, n, larg)
  
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)
  
arr = list(map(int,input().split()))
heapSort(arr)
n = len(arr)
print('Sorted array is')
print(*arr)