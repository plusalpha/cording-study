
#사람 클래스의 기본 요소 - 이름, 나이, 성별
#직장 동료 클래스를 사람 클래스를 이용해서 만들기 - 별도 추가 사항 직급

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # def about_me(self):
    #     print("내 이름은 " + self.name + "이고 " + "내 나이는 " + self.age + "살 입니다!")


person_1 = Person("김미영", "31", "여자")
person_2 = Person("김성규", "29", "남자")

print(person_1.name)
# person_1.about_me()
# person_2.about_me()


class Employee(Person):
         position = "대리"

#고급
class Employee(Person):
    def __init__(self, name, age, gender, position):
        Person.__init__(self, name, age, gender)
        self.position = position
    # def about_me(self):
    #     Person.about_me(self)
    #     print("나의 직급은 " + self.position + "입니다.")



employee_1 = Employee("김미영", "31", "여자", "팀장")
employee_2 = Employee("김성규", "29", "남자", "사원")

print(employee_1.age)
print(employee_2.position)
# employee_1.about_me()
