class Shape:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def get_area(self):
        print('도형의 면적을 출혁합니다.')

class Circle(Shape):
    def __init__(self,x,y,radius):
        super().__init__(x,y)
        self.radius=radius

    def get_area(self):
        import math
        return math.pi *self.radius*self.radius

class Cilinder(Circle):
    def __init__(self,x,y,radius,height):
        super().__init__(x,y)
        self.radius=radius
        self.height=height

    def get_area(self):
        import math
        return math.pi *self.radius*self.radius*self.height

class Rectangle(Shape):
    def __init__(self,x,y,width,height):
        super().__init__(x,y)
        self.width=width
        self.height=height

    def get_area(self):
        import math
        return self.width*self.height

    def __add__(self, other):
        #두사각형의 길이의 합.
        return  Rectangle(0,0,(self.width+other.width),(self.height+other.height))
        #두 사각형의 넓이의 합
        # return(self.width*self.height)+(other.width * other.height)
    #여기서 r1이 self r2가 other

    def __repr__(self):
        return f'사각형의 좌표는 x:{self.x}, y:{self.y}이고 넓이는 {self.get_area()}입니다.'

c1=Circle(100,100,10.0)
c2=Circle(50,50,2.0)
r1=Rectangle(100,50,5,2)
r2=Rectangle(0,0,10,15)

print(r1.get_area())
print(c1.get_area())
print(c2.get_area())

#print(r1+r2) #갑자기 두개의 사각형의 합을 구하라고 하면 동작할리가 없음.
#r1.add(r2) 랑 같은 의미임.

# class Pokemon:
#     def __init__(self, name,owner,skills): #객체 생성시 동작.
#         self.name = name
#         self.owner = owner
#         self.skills = skills.split('/')
#         print(f'pokemon {name} created')
#
#     def info(self):
#         #self.하면 현재 객체의 ~~속성이라는 의미
#         print(f'{self.owner}의 포켓몬은 {self.name}입니다.')
#         print(f'{self.owner}의 포켓몬이 사용가능한 스킬:')
#         for skill in self.skills:
#             print(skill)
#     def attack(self,idx):
#         print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격시전')
#
#
# p1 = Pokemon('pikachu','한지우','50만 볼트/100만 볼트/번개')
# p2 = Pokemon('turtle','오바람','고속스핀/거품/몸통박치기/하이드로펌프')
#
# p1.info()
# p2.info()
#
# class Pikachu(Pokemon): #inheritance
#     def __init__(self, owner, skills):
#         # 생성자 오버라이드
#         super().__init__(self, owner, skills)
#         # super()로 부모의 print문을 가져온다.
#         print(f'Pikachu')
#
#     def attack(self, idx):
#         print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격시전')
#
# pi1 = Pikachu('덴트','번개')
# pi1.info()
# class Ggobugi(Pokemon): #inheritance
#     def __init__(self,owner,skills):
#         #생성자 오버라이드
#         super().__init__(self,owner,skills)
#         #super()로 부모의 print문을 가져온다.
#         print(f'Ggobugi')
#     def attack(self,idx):
#         print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격시전')
#
# class Pairi(Pokemon): #inheritance
#     def __init__(self,owner,skills):
#         #생성자 오버라이드
#         super().__init__(self,owner,skills)
#         #super()로 부모의 print문을 가져온다.
#         print(f'Ggobugi')
#     def attack(self,idx):
#         print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격시전')
#
# ggo1=Ggobugi('Ohbaram','고속스핀/거품/몸통박치기/하이드로펌프')
# ggo1.info()
# ggo1.attack(1)

