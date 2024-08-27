def subtotal(current_speed):
    return sum([i for i in range(1, current_speed)])

def is_ok_to_maintain_speed(x, current_speed, distance):
    if x - subtotal(current_speed) - distance - current_speed >= 0:
        return True
    return False

x = int(input())

# 제동하는 동안의 거리가 도착지를 넘지 않는 한 가속 가능
current_speed = 1 # 1초 지점, 1m/s
distance = 1 # 1초 지점, 1m
while x - subtotal(current_speed+1) - (distance + current_speed + 1) >= 0:
    current_speed += 1
    distance += current_speed

t = current_speed
# 최고 속도를 얼마나 유지해도 되는지 체크
while True:
    if current_speed == 1:
        break
    if not is_ok_to_maintain_speed(x, current_speed, distance):
        current_speed -= 1
    t+=1
    distance += current_speed

print(t + (x-distance))