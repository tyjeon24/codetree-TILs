a = int(input())

for i in range(1, a+1):
    even_and_not_4mul = i % 2==0 and i%4
    div8_quotient_is_even = (i//8)%2==0
    div7_remainder_lessthan_4 = (i%7) < 4
    if not even_and_not_4mul and not div8_quotient_is_even and not div7_remainder_lessthan_4:
        print(i, end=" ")