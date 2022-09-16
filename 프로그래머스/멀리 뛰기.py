def solution(n):
    #규칙이 있나 n을 1부터 구해봄
    #n = 1 , 1  n = 4, 5
    #n = 2 , 2  n = 5, 8
    #n = 3, 3   n = 6, 13
    #n= 1 3 4 5 6 // 1 2 3 5 8 13 ->피보나치 규칙
    answer = 0
    if n<=2:
        return n
    a = 1
    b = 2
    for i in range(2, n):
        a, b = b, a+b
    answer = b % 1234567
    return answer
