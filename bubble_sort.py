def bubble_sort(arr):
    total_length=len(arr)
    for i in range(total_length):
        for j in range(0, total_length - i - 1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


arr = [20,10,50,40,60,30]
print("Unshorted Array : ",arr)
print("Shorted Aarray : ", bubble_sort(arr))