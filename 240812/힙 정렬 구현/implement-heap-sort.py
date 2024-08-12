n = int(input())
arr = list(map(int, input().split()))
arr = [0] + arr

def heapify(n, i):
    largest = i
    l = i*2
    r = i*2+1

    for node in [l, r]:
        if node <= n and arr[node] > arr[largest]:
            largest = node
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(n, largest)

def heap_sort(arr):
    for i in range(n//2, 0, -1):
        heapify(n, i)
    for i in range(n, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(i-1, 1)


heap_sort(arr)
for num in arr[1:]:
    print(num, end=" ")