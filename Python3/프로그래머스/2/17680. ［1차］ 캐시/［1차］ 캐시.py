from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    time = 0
    cache = deque(maxlen=cacheSize)

    for city in cities:
        name = city.lower()
        if name in cache:
            cache.remove(name)
            cache.append(name)
            time += 1
        else:
            cache.append(name)
            time += 5
            
    return time