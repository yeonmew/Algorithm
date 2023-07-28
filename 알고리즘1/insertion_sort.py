import time
import random
import numpy as np

def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1): #끝에서부터 역순으로 반복한다.
            if arr[i - 1] > arr[i]: #이전의 원소가 다음의 원소보다 크면 서로 바꾼다.
                arr[i - 1], arr[i] = arr[i - 1], arr[i]
    return arr

#  1) 1~1000만까지 순서대로 숫자가 저장된 배열
arr = np.array([])
arr = np.array(range(1, 10000000)) #1~1000만까지 arr에 저장

time1 = time.time()
insertion_sort(arr)
print('1~1000만까지 순서대로 숫자가 저장된 배열 시간 측정  =   ', time.time() - time1)

#  2) 1000만~1까지 순서대로 숫자가 저장된 배열
arr = np.array([]) #배열 초기화 후 다시 진행
arr = np.array(range(10000000,1,-1)) #1000만~1까지 arr에 저장

time2 = time.time()
insertion_sort(arr)
print('1000만~1까지 순서대로 숫자가 저장된 배열 시간 측정  =   ', time.time() - time2)

#  3) 균등하게 섞여있는 배열(크기는 1000만)
arr = np.array([]) #배열 초기화 후 다시 진행
for i in range(1, 10000000):
    arr = np.append(arr, np.array(random.randint(1,10000000)))

time3 = time.time()
insertion_sort(arr)
print('균등하게 섞여있는 배열(크기는 1000만) 시간 측정  =   ', time.time() - time3)