#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 22:33:30 2022

@author: thaibinhbr97
"""

import random

def is_sorted(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

def bogo_sort(L):
    # count = 0
    while not is_sorted(L):
        # count += 1
        # print(count)
        random.shuffle(L)
        
L = [4,1,9,10,3,2,100]
bogo_sort(L)
        
def bubble_sort(L):
    swap = False
    while not swap:
        # print(L)
        swap = True
        for i in range(1,len(L)):
            if L[i-1] > L[i]:
                swap = False
                temp = L[i]
                L[i] = L[i-1]
                L[i-1] = temp

L1 = [1,5,3,8,4,9,6,2]                
# bubble_sort(L1)


def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            print(L)
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

L2 = [1,5,3,8,4,9,6,2] 
# selection_sort(L2)

def selSort(L):
    """
    selSort:

    You can sort a list by always moving the smallest element from the unsorted list 
    to a new list. That procedure would add the elements to the new list in 
    increasing order, and when every element from the old list has been moved over, 
    we end up with a new sorted list. This type of sorting algorithm is often called 
    Selection Sort.
    selSort implements this without explicitly creating a new list, by maintaining 
    sorted (from position 0 to i-1) and unsorted (from position i to the end) parts 
    of the list. All elements in positions before the iterating variable i are 
    sorted, and unsorted for those positions at i or below. In each iteration, it 
    selects the smallest element in the unsorted part of the list, and swaps it 
    with the element at the ith position. That essentially adds the next smallest 
    element from the old list and appends it to the new. It keeps doing that until 
    the old list is empty (i.e., i reaches the end of the list).
    """
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
            
def newSort(L):
    """
    newSort:

    newSort is basically a slight variant of Selection Sort. In each iteration,
    newSort also tries to find the smallest element in the unsorted part of the
    list and appends it to the sorted part of the list. The only difference here
    is that instead of finding the smallest value in the unsorted part of the list
    with minVal and minIndx, newSort maintains that the element at the ith position
    is the smallest element between the ith and jth positions. So, when j reaches
    the end of the list, the ith position must have been the smallest element in
    the unsorted portion (from position i to the end) of the list.
    """
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
            
def newSort1(L):
    """ L, list with unique elements """
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
            
def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # when right sublist is empty
    while i < len(left):
        result.append(left[i])
        i += 1
    # when left sublist is empty
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

L3 = [4,5,2]
L4 = [1,3,6]
print(merge(L3,L4))


def merge_sort(L):
    # base case
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        # divide
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        # conquer with merge step
        return merge(left, right)
    
def swapSort(L): 
    """ 
    L is a list on integers 
    sorting in ascending order
    """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

L3 = [4,5,2]
swapSort(L3)

def modSwapSort(L): 
    """ 
    L is a list on integers 
    sorting in descending order
    """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)

modSwapSort(L4)
modSwapSort(L3)

# L5 = [1,2,3,4,5,6]
# swapSort(L5)
# modSwapSort(L5)
# swapSort(L5)

