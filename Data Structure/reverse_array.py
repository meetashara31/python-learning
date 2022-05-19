def reverse1(arr : list):
    n = len(arr)

    for i in range(0, int((n-1)/2)):
        swap(i, n-1-i, arr)



def swap(i1, i2, arr):
    t = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = t

if __name__ == "__main__":
    arr = [453, 345, 75, 948, 43, 865, 87, 9865, 547, 88429, 309727, 65, 85, 498, 7, 23]

    # print(arr)

    reverse1(arr)

    print(arr)