# 프로그램명: 성적이 낮은 순서로 학생 출력하기
# 작성자: yeonmew
# 작성일: 23.02.15

#N을 입력받는다.
n = int(input())

#N명의 학생 정보를 입력받아 리스트에 저장한다.
arr = []
for i in range(n):
    data = input().split()
    #이름은 문자열 그대로, 점수는 정수형으로 변환해 저장한다.
    arr.append((data[0], int(data[1])))

#키를 이용하여, 점수를 기준으로 정렬한다.
arr = sorted(arr, key = lambda student: student[1])

#정렬이 수행된 결과를 출력한다.
for student in arr:
    print(student[0], end = ' ')