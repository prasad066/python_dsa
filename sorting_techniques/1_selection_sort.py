def printarray(arr):
    for ele in arr:
        print(ele,end=" ")
    print()
def selectionsort(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if arr[min_idx]>arr[j]:
                min_idx =j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
if __name__ == "__main__":
    arr=[1,9,2,8,3,7,4,6,5]
    print("original array :",end="")
    printarray(arr)
    selectionsort(arr)
    print("sorted array :",end="")
    printarray(arr)
    
    