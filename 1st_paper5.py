# 검색할 구구단의 숫자를 입력 받으면 해당 단의 구구단을 보여줌
# 구구단은 2~9단까지만 나오고 그 외의 숫자를 입력하면 해당 메세지 출력
# 2단 과 같이 문자를 넣는 경우 발생하는 오류 처리와 함께 다시 구구단이 실행되도록 구현

def multiplication():
    try:
        dan = int(input("몇 단을 출력해주시겠습니까?"))
        if 1 < dan and dan < 10:
            for num in range(1, 10):
                print("{} * {} = {}".format(dan,num,dan*num))
        else:
            print("구구단은 2~9단까지만 입력 가능합니다.")
            return multiplication()
    except ValueError:
            print("2에서 9사이의 숫자만 입력해주세요.")
            return multiplication()

result = multiplication()

result
