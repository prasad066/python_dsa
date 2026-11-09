def printarray(arr):
    for ele in arr:
        print(ele,end=" ")
    print()
def bubblesort(arr):
    n=len(arr)
    swapped=False
    for i in range(n):
        printarray(arr)
        swapped=True
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=False
        if swapped==True:
            break
if __name__ == "__main__":
    arr=[1,9,2,8,3,7,4,6,5]
    print("original array :",end="")
    printarray(arr)
    bubblesort(arr)
    print("sorted array :",end="")
    printarray(arr)
    
    