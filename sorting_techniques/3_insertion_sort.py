def printarray(arr):
    for ele in arr:
        print(ele,end=" ")
    print()
def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        max_idx=i
        for j in range(i-1,-1,-1):
            if arr[max_idx]<arr[j]:
                arr[max_idx],arr[j]=arr[j],arr[max_idx]
                max_idx=j
if __name__ == "__main__":
    arr=[1,9,2,8,3,7,4,6,5]
    print("original array :",end="")
    printarray(arr)
    insertionsort(arr)
    print("sorted array :",end="")
    printarray(arr)
    
    