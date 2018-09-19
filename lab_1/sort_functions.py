
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
import numpy as np
import sys
import time


# In[ ]:


def merge_sort(A):
    merge_sort2(A, 0, len(A)-1)

def merge_sort2(A, first, last):
    if first < last:
        middle = (first + last)//2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle+1, last)
        merge(A, first, middle, last)

def merge(A, first, middle, last):
    L = A[first:middle+1]
    R = A[middle+1:last+1]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = j = 0

    for k in range (first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


# In[2]:



def quick_sort(A):
    quick_sort2(A, 0, len(A)-1)

def quick_sort2(A, low, hi):
    if low < hi:
        p = partition(A, low, hi)
        quick_sort2(A, low, p - 1)
        quick_sort2(A, p + 1, hi)

def partition(A, low, hi):
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]
    border = low

    for i in range(low, hi+1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]

    return (border)


def get_pivot(A, low, hi):
    mid = (hi + low) // 2
    s = sorted([A[low], A[mid], A[hi]])
    if s[1] == A[low]:
        return low
    elif s[1] == A[mid]:
        return mid
    return hi


def quick_selection(x, first, last):
    for i in range (first, last):
        minIndex = i
        for j in range (i+1, last+1):
            if x[j] < x[minIndex]:
                minIndex = j
        if minIndex != i:
            x[i], x[minIndex] = x[minIndex], x[i]

