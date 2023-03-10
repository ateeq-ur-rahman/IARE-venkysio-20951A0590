/*
 * 
 * Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping the digits of each key by individual digits. The sort begins by sorting the least significant digit of each number, and working its way up to the most significant digit. 
 * It is based on the idea of sorting the input data based on the digits in its individual positions.
 * 
 * Here is the algorithm for Radix sort:

Find the maximum number in the array.
Count the number of digits in the maximum number.
For each digit from right to left, do the following:
a. Initialize a count array of size 10 (since there are 10 possible digits) with all elements set to 0.
b. Traverse the input array and count the number of times each digit appears at the current position.
c. Modify the count array to store the running sum of the counts so that each element stores the total count of numbers with that digit or lower.
d. Create a temporary array to store the sorted output.
e. Traverse the input array from right to left and, for each element, use the count array to determine the correct position of that element in the temporary array.
f. Copy the elements from the temporary array back into the input array.
The input array is now sorted.
Radix sort has a time complexity of O(d*(n+b)) where d is number of digits and n is number of elements in array.


EG:
Input is 329,457,657,839,436,720,355

329    720    720    329
457    355    329    355
657    436    436    436
839 --->457 -->839 -->457
436    657    355    657
720    329    457    720
355    839    657    839
 */

//CODE

// Radix sort Java implementation

import java.io.*;
import java.util.*;

class radixsort {
    static int getMax(int arr[], int n)
    {
        int mx = arr[0];
        for (int i = 1; i < n; i++)
            if (arr[i] > mx)
                mx = arr[i];
        return mx;
    }

    static void countSort(int arr[], int n, int exp)
	{
		int ou[] = new int[n]; 
		int i;
		int kc[] = new int[10];
        Arrays.fill(kc, 0);
        for (i = 0; i < n; i++)
			kc[(arr[i] / exp) % 10]++;
		for (i = 1; i < 10; i++)
			kc[i] += kc[i - 1];		
		for (i = n - 1; i >= 0; i--) {
			ou[kc[(arr[i] / exp) % 10] - 1] = arr[i];
			kc[(arr[i] / exp) % 10]--;
		}		
		for (i = 0; i < n; i++)
			arr[i] = ou[i];
	}	
	static void radixsort(int arr[], int n)
	{	
		int m = getMax(arr, n);
		for (int exp = 1; m / exp > 0; exp *= 10)
			countSort(arr, n, exp);
	}	
	static void print(int arr[], int n)
    {
        for (int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
    }

    public static void main(String[] args)
	{
		int arr[] = {1,56,24,85,95,75};
		int n = arr.length;

		
		radixsort(arr, n);
		print(arr, n);
	}
}
