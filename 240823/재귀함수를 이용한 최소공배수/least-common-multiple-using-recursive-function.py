n = int(input())
arr = list(map(int, input().split()))

def calculate(arr, lcm=None, index=1):
    if index==1:
        lcm = arr[0]

    for num in range(min([lcm, arr[index]]),0,-1):
        if lcm % num == 0 and arr[index] % num == 0:
            lcm = int(lcm * arr[index] / num)
            break
    if index == len(arr)-1:
        return lcm
    calculate(arr, lcm, index+1)
print(calculate(arr))