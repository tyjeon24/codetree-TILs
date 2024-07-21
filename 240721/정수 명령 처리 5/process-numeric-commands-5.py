N = int(input())

number_list = []

for command in range(N):
    order_set = input()
    if order_set.startswith("push_back"):
        number_list.append(int(order_set.split()[1]))
    elif order_set.startswith("get"):
        print(number_list[int(order_set.split()[1])-1])
    elif order_set.startswith("size"):
        print(len(number_list))
    elif order_set.startswith("pop_back"):
        number_list.pop()