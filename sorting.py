import random

def insertion_sort(arr):
    pos = 1 
    while pos < len(arr):
        key = arr[pos]
        i = pos - 1
        while(i >= 0 and arr[i] > key):
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
        pos += 1


