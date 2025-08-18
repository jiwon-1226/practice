#부모 클래스(super class)
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 동물객체 생성")

    def speak(self):
        print(f"{self.name}가 소리를 냅니다")

    def move(self):
        print(f"{self.name}가 움직입니다")

#=========상속 시작=======
#자식 클래스 (sub class)
#괄호 안에 부모 클래스 이름을 명시해서 상속 선언
class Dog(Animal):
    def wag(self):
        print(f"{self.name}가 꼬리를 흔듭니다")

    def speak(self): #부모 클래스의 speak 메소드를 재정의(overriding)
        print("왈왈")

class Cat(Animal):
    def speak(self):
        print("애옹")

    def climb(self):
        print(f"{self.name}가 높은 곳에 올라갔습니다")

animal1 = Animal("객체")
animal1.move()

dog1 = Dog("방울이")
dog1.wag()
dog1.speak()
dog1.move()

cat1 = Cat("애용이")
cat1.speak()
cat1.climb()

#실습
#shape 라는 부모 클래스 => color
#메소드 describe => 이 도형의 색깔은 - 입니다 출력

#Circle 자식 클래스
#메소드 describe 오버라이딩 => 이 원의 색깔은 - 입니다
#메소드 get_area(radius) => math.pi 모듈을 이용해서 넓이 구해서 리턴
#리턴한 것을 print로 출력시 소수점 둘째자리까지

import math

class Shape:
    def __init__(self, color):
        self.color = color
    def describe(self):
        print(f"이 도형의 색깔은 {self.color}입니다")

class Circle(Shape):
    def describe(self):
        print(f"이 원의 색깔은 {self.color}입니다")
    def get_area(self, radius):
        return math.pi * (radius ** 2)


cir = Circle("red")
cir.describe()
print(f"원의 넓이 : {cir.get_area(5):.2f}")









