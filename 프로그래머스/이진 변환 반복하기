def solution(s):
    answer = []
    cnt = 0 #나중에 1까지 될때까지 횟수 +1
    tmp = 0
    while True:
        if s == '1':
            break
        tmp = tmp + s.count("0")
        s = s.replace("0","")
        
        s = bin(len(s))[2:] #0b없애려고 [2:]
        cnt = cnt +1
    answer = [cnt, tmp]
    # # s = 110010101001
    # s = s.replace("0","")
    # #print(s) #111111 #길이가 6 -> 110만들기
    # s = bin(len(s))[2:] # 110
    # print(s)
    return answer
