def solution(n):
    answer = 0
    a=0
    b=1
    for i in range(2, n+1):
        a, b = b, a+b
    answer = b % 1234567
    
    return answer
  #복습
  #앞의 문제랑 동일한 방법
