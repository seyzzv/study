
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    current_weight = 0
    time = 0

    for truck in truck_weights:
        while True:
            time += 1
            current_weight -= bridge.popleft()

            if current_weight + truck <= weight:
                bridge.append(truck)
                current_weight += truck
                break
            else:
                bridge.append(0)

    return time + bridge_length