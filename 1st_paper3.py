# 사용자에게 가위, 바위, 보 중 하나를 묻기
# 사용자가 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가른다.
# 다 합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝남

import random

Rock = "바위"
Scissors = "가위"
Paper = "보"

game = [Rock, Scissors, Paper]






u_win = 0
c_win = 0

while u_win < 3 and c_win < 3:

    user_c = input("{}, {}, {} 중 하나 내기 : ".format(Rock,Scissors,Paper))
    com_c = random.choice(game)

    if user_c == com_c:
        user_c
        print("컴퓨터 : " + com_c)
        u_win = c_win
        u_win = c_win
        print("현재 스코어{}:{}".format(u_win, c_win))
    elif user_c == Scissors:
        if com_c == Paper:
            user_c
            print("컴퓨터 : " + com_c)
            c_win = c_win + 1
            print("현재 스코어{}:{}".format(u_win, c_win))
        elif com_c == Rock:
            user_c
            print("컴퓨터 : " + com_c)
            c_win = c_win + 1
            print("현재 스코어{}:{}".format(u_win, c_win))
    elif user_c == Paper:
        if com_c == Rock:
            user_c
            print("컴퓨터 : " + com_c)
            c_win = c_win + 1
            print("현재 스코어{}:{}".format(u_win, c_win))
        elif com_c == Scissors:
            user_c
            print("컴퓨터 : " + com_c)
            c_win = c_win + 1
            print("현재 스코어{}:{}".format(u_win, c_win))
    elif user_c == Rock:
        if com_c == Scissors:
            user_c
            print("컴퓨터 : " + com_c)
            u_win = u_win + 1
            print("현재 스코어{}:{}".format(u_win, c_win))
        elif com_c == Paper:
            user_c
            print("컴퓨터 : " + com_c)
            c_win = c_win + 1
            print("현재 스코어{}:{}".format(u_win, c_win))
    else:
        print("가위 바위 보 중 하나를 정확히 입력해주세요.")






#중복 코드 분리 실패


# class WhoWin():
#     u_win = 0
#     c_win = 0
#     user_c = input("{}, {}, {} 중 하나 내기 : ".format(Rock,Scissors,Paper))
#     com_c = random.choice(game)
#     def user_win(self):
#         self.user_c
#         print("컴퓨터 : " + com_c)
#         self.u_win = self.u_win + 1
#         print("현재 스코어{}:{}".format(u_win, self.c_win))
#     def com_win(self):
#         self.user_c
#         print("컴퓨터 : " + self.com_c)
#         self.c_win = self.c_win + 1
#         print("현재 스코어{}:{}".format(self.u_win, self.c_win))
#
# who = WhoWin()
#
#
#
#
# who.u_win
# who.c_win
#
# while who.u_win < 3 and who.c_win < 3:
#
#     who.user_c
#     who.com_c
#
#     if who.user_c == who.com_c:
#         who.user_c
#         print("컴퓨터 : " + who.com_c)
#         who.u_win = who.c_win
#         who.u_win = who.c_win
#         print("현재 스코어{}:{}".format(who.u_win, who.c_win))
#     elif who.user_c == Scissors:
#         if who.com_c == Paper:
#             who.user_win
#         elif who.com_c == Rock:
#             who_com_win
#     elif who.user_c == Paper:
#         if who.com_c == Rock:
#             who.user_win
#         elif who.com_c == Scissors:
#             who_com_win
#     elif who.user_c == Rock:
#         if who.com_c == Scissors:
#             who.user_win
#         elif who.com_c == Paper:
#             who.com_win
#     else:
#         print("가위 바위 보 중 하나를 정확히 입력해주세요.")



#가위 바위 보가 아닌 다른 문자를 입력했을 경우도 대응하도록 구현 X


# u_win = 0
# c_win = 0
# while u_win < 3 and c_win < 3:
#
#     com_c = random.choice(game)
#     user_c = input("{}, {}, {} 중 하나 내기 : ".format(Rock,Scissors,Paper))
#
#     if user_c == com_c:
#         user_c
#         print("컴퓨터 : " + com_c)
#         u_win = u_win
#         c_win = c_win
#         print("현재 스코어{}:{}".format(u_win, c_win))
#     elif user_c == Scissors and com_c == Paper:
#         user_c
#         print("컴퓨터 : " + com_c)
#         u_win = u_win + 1
#         print("현재 스코어{}:{}".format(u_win, c_win))
#     elif user_c == Paper and com_c == Rock:
#         user_c
#         print("컴퓨터 : " + com_c)
#         u_win = u_win + 1
#         print("현재 스코어{}:{}".format(u_win, c_win))
#     elif user_c == Rock and com_c == Scissors:
#         user_c
#         print("컴퓨터 : " + com_c)
#         u_win = u_win + 1
#         print("현재 스코어{}:{}".format(u_win, c_win))
#     else:
#         user_c
#         print("컴퓨터 : " + com_c)
#         c_win = c_win + 1
#         print("현재 스코어{}:{}".format(u_win,c_win))





if u_win == 3:
    print("{} 대 {}로 당신이 이겼습니다".format(u_win,c_win))
elif c_win == 3:
    print("{} 대 {}로 당신이 졌습니다".format(u_win,c_win))
