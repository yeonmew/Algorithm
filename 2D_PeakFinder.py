import random

def peak_finder(arr):
    max(map(max,arr))



arr = [[random.randint(1,100) for j in range(5)] for i in range(5)]

print(arr)
print(max(map(max,arr)))
