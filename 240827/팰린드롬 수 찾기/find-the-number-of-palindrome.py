low, high = map(int, input().split())

def is_palindrome(number):
    number = str(number)
    for i in range(len(number)//2):
        left = number[i]
        right = number[-i-1]
        if left != right:
            return False
    return True

result = 0
for number in range(low, high+1):
    if is_palindrome(number):
        result += 1
print(result)