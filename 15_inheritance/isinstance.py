from pdb import line_prefix

from inheritance import Animal, Dog

dog1 = Dog("방울이")
#isinstance(객체, 클래스): 객체가 해당 클래스 또는 부모 클래스의 인스턴스인지 확인
print(isinstance(dog1, Dog))
print(isinstance(dog1, Animal))

animal1 = Animal("동물")
print(isinstance(animal1, Dog))
print(isinstance(animal1, Animal))

#Person 클래스, Student 클래스, Teacher 클래스
#person 속성으로 name
#student 속성으로 grade
#teacher 속성으로 subject

#일반 함수 정의
#매개변수로 클래스의 객체를 넣으면 if문으로 student 클래스의 객체이면
#***학년 학생입니다
#teacher 클래스면 **과목 선생님입니다.
#person이면 일반 시민입니다

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

def process_person(obj):
    if isinstance(obj, Student):
        print(f"{obj.grade}학년 {obj.name}학생입니다")
    elif isinstance(obj, Teacher):
        print(f"{obj.subject}과목 {obj.name}선생님입니다")
    elif isinstance(obj, Person):
        print(f"일반 시민 {obj.name}입니다")
    else:
        print("알 수 없는 타입의 객체입니다")

p1 = Person("사람")
S2 = Student("고딩", 3)
T3 = Teacher("쌤", "python")
process_person(p1)
process_person(T3)

str1 = "abc"
process_person(str1)

# def process_person(name):
#     if isinstance(name, Student) is True:
#         print(f"{name.grade}학년 학생입니다")
#     elif isinstance(name, Teacher) is True:
#         print(f"{name.subject}과목 선생님입니다")
#     else:
#         print("일반 시민입니다")