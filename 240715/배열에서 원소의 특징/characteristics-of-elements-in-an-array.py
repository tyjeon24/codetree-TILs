front_element = None
for number in map(int, input().split()):
    if number % 3 == 0 and front_element:
        print(front_element)
        break
    front_element = number