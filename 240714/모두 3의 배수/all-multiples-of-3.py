all_numbers_3mul = 1
for i in range(5):
    if int(input())%3!=0:
        all_numbers_3mul = 0
        break
print(all_numbers_3mul)