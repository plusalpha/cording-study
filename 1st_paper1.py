# 파이썬 파일 실행 시키면, 한식, 중식, 일식 중 한가지를 고르는 질문
# 그 중 한 가지를 고르면 식당 이름을 하나 임의로 추천

import random

food = input("한식, 중식, 일식 중 한 가지를 고르세요. 음식점을 추천해 드립니다 : ")

kfood = ["자연밥상", "본비빔밥", "조마루감자탕", "백로식당","자연별곡"]
jfood = ["스시김", "일본식", "키햐아", "고베규카츠"]
cfood = ["베이징", "극동반점", "북경깐풍기", "황궁쟁반짜장"]


if food == "한식":
    print(random.choice(kfood))
elif food == "일식":
    print(random.choice(jfood))
elif food == "중식":
    print(random.choice(cfood))
else:
    print("한식, 일식, 중식 중에서 하나만 선택하세요.")
