

# 사용자로부터 몇 단을 출력할 지 받을 것
# 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것

# 1) while문 (구두 설명 듣기 전)

#ques = input("몇 단을 출력 하시겠습니까?")
# dan = 1
#
# if 1 < int(ques) and int(ques) < 10:
#
#     while dan < 10:
#         print(ques + " * " + str(dan) + " = " + str(int(ques) * dan))
#         dan = 1 + dan
#
# else:
#     print("구구단은 2~9단까지만 입력 가능합니다.")


# 2) for문

# if 1 < int(ques) and int(ques) < 10:
#
#     for num in range(1, 10):
#         print(ques + " * " + str(num) + " = " + str(int(ques) * num))
#
# else:
#     print("구구단은 2~9단까지만 입력 가능합니다.")

#강의

dan = int(input("몇 단을 출력 하시겠습니까?"))

if 1 < dan and dan < 10:

    for num in range(1, 10):
        print("{} * {} = {}".format(dan,num,dan * num))
    #문자열을 하나의 포멧으로 만들어 빈 중괄호에는 각 결과 값를 넣도록 한다.
else:
    print("구구단은 2~9단까지만 입력 가능합니다.")
