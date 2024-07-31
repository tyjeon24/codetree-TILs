def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    left, right = arr[low:mid+1], arr[mid+1:high+1]
    l, r = 0, 0
    i = low

    while l != len(left) or r != len(right):
        if l == len(left):
            arr[i] = right[r]
            r+=1
        elif r == len(right):
            arr[i] = left[l]
            l+=1
        elif left[l] < right[r]:
            arr[i] = left[l]
            l+=1
        else:
            arr[i] = right[r]
            r+=1
        i+=1

arr = [5,2,6,1,3,8]
merge_sort(arr, 0, 5)
for i in arr:
    print(i, end=" ")