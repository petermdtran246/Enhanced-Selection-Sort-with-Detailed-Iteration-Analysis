# Enhanced Selection Sort with Detailed Iteration Analysis

This repository contains a Python implementation of the selection sort algorithm modified to meet specific requirements for an assignment. The goal is to sort an array into ascending order with the following modifications:

  1.  After k iterations through the outer loop, the k largest elements should be sorted rather than the k smallest elements.
  2.  On each iteration through the outer loop, count the number of times two array elements are compared and the number of times two array elements are swapped.
  3.  Reinitialize these counters to zero at the beginning of each iteration. After each iteration through the outer loop, print three things: the partially sorted array, the number of comparisons on this iteration, and the number of swaps on this iteration. After the kth iteration, you should see that the k largest elements have been placed into the last k slots of the array.

# Problem Instances
The modified selection sort algorithm is tested on the following arrays:

  -  A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
  -  A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
  -  A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]

# Code
The main script selection_sort.py contains the implementation of the selection sort algorithm with the required modifications.
