n = int(input())
arr = list(map(int, input().split()))


def radix_sort(arr, k):
    for pos in range(k, -1, -1):
        arr_new = [[] for _ in range(10)]
        for i in range(0, len(arr)):
            digit = arr[i] % (10 ** (k-pos+1))
            arr_new[digit].append(arr[i])
        
        store_arr = []
        for i in range(0, 10):
            for j in range(0, len(arr_new[i])):
                store_arr.append(arr_new[i][j])
        arr = store_arr
    return arr

max_value = max(arr)
k=0
while max_value != 0:
    max_value //= 10
    k+=1


for number in radix_sort(arr, k):
    print(number, end=" ")