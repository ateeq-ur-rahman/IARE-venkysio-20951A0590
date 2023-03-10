/*
 * 
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

Max-Heapify -- Algo 
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
 */

//CODE
public class  heapsort{
	public void sort(int[] array) {
        int n = array.length;
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(array, n, i);
        for (int i = n - 1; i >= 0; i--) {
            int temp = array[0];
			array[0] = array[i];
            array[i] = temp;
            heapify(array, i, 0);
		}
	}

	
	void heapify(int[] array, int n, int i) {
		int lar = i; 
		int left = 2 * i + 1; 
        int right = 2 * i + 2;
        if (left < n && array[left] > array[lar])
            lar = left;
        if (right < n && array[right] > array[lar])
            lar = right;
        if (lar != i) {
			int swap = array[i];
			array[i] = array[lar];
            array[lar] = swap;
            heapify(array, n, lar);
		}
	}

	
	static void printArray(int[] array) {
		int n = array.length;
		for (int i = 0; i < n; ++i)
			System.out.print(array[i] + " ");
		System.out.println();
	}

	
	public static void main(String[] args) {
        int[] array = { 13, 4, 5, 12, 6 };
		int n = array.length;

		heapsort ob = new heapsort();
		ob.sort(array);

		System.out.println("Sorted array is");
		printArray(array);
	}
}


