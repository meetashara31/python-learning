from audioop import minmax
from tkinter.tix import ExFileSelectBox

from pandas import array


class Pair:
    def __init__(self) -> None:
        self.min = 0
        self.max = 0

## METHOND 1 - Linear Search ## O(n)
def getMinMax(arr: list) -> Pair:
    minmax = Pair()
    n = arr.__len__()

    if(n == 1):
        minmax.min = arr[0]
        minmax.max = arr[0]
        return minmax

    if(arr[0] > arr[1]):
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2, n):
        if(arr[i] > minmax.max):
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax

## OTHER METHOD - Recursion ## O(logn)
def getMinMax2(low: int, high: int, arr: list):
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)
         
    # If there is only two element
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)

    else:
        mid = int((low+high)/2)
        arr_max1, arr_min1 = getMinMax2(low, mid, arr)
        arr_max2, arr_min2 = getMinMax2(mid+1, high, arr)
        
        return max(arr_max1, arr_max2), min(arr_min1, arr_min2)

def getMinMax3(arr):
    n = len(arr)

    if(n%2 == 0):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])

        i = 2
    else:
        mx = mn = arr[0]
        i = 1
    
    while(i < n-1):
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i+1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])

        i += 2

    return(mx, mn)

if __name__ == "__main__":
    arr = [453, 345, 75, 948, 43, 865, 87, 9865, 547, 88429, 309727, 65, 85, 498, 7]
    # minmax = getMinMax(arr)
    # a, b = getMinMax2(0, 5, arr)
    mx, mn = getMinMax3(arr)

    print('Min: ', mn)
    print('Max: ', mx)