# 사용자에게 가위, 바위, 보 중 하나를 묻기
# 사용자가 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가른다.
# 다 합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝남

import random

Rock = "바위"
Scissors = "가위"
Paper = "보"

game = [Rock, Scissors, Paper]



# 시간이 조금 더 있었으면 사용자가 가위 바위 보가 아닌 다른 문자를 입력했을 경우도 대응하도록 구현하는 것도 더 고민해봤을 텐데 우선 제출합니다.

# def user_chocie():
#     user = input("{}, {}, {} 중 하나 내기 : ".format(Rock,Scissors,Paper))
#     if user != "가위" or user != "바위" or user != "보":
#         print("가위, 바위, 보 중 하나만 선택하세요")
#     return user_chocie()
#
# user_c = user_chocie()




u_win = 0
c_win = 0

while u_win < 3 and c_win < 3:
    user_c = input("{}, {}, {} 중 하나 내기 : ".format(Rock,Scissors,Paper))
    com_c = random.choice(game)

    if user_c == com_c:
        user_c
        print("컴퓨터 : " + com_c)
        u_win = u_win
        c_win = c_win
        print("현재 스코어{}:{}".format(u_win, c_win))
    elif user_c == Scissors and com_c == Paper:
        user_c
        print("컴퓨터 : " + com_c)
        u_win = u_win + 1
        print("현재 스코어{}:{}".format(u_win, c_win))
    elif user_c == Paper and com_c == Rock:
        user_c
        print("컴퓨터 : " + com_c)
        u_win = u_win + 1
        print("현재 스코어{}:{}".format(u_win, c_win))
    elif user_c == Rock and com_c == Scissors:
        user_c
        print("컴퓨터 : " + com_c)
        u_win = u_win + 1
        print("현재 스코어{}:{}".format(u_win, c_win))
    else:
        user_c
        print("컴퓨터 : " + com_c)
        c_win = c_win + 1
        print("현재 스코어{}:{}".format(u_win,c_win))





if u_win == 3:
    print("{} 대 {}로 당신이 이겼습니다".format(u_win,c_win))
elif c_win == 3:
    print("{} 대 {}로 당신이 졌습니다".format(u_win,c_win))
