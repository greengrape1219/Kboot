#generator

def a(): #generator in part of function
    yield 1
    yield 2
    yield 3

def b(): #standard function
    return 1
    return 2

print(a(),b())
c=a() #c is object of generator
for s in c:
    print(s)

for s in c:
    print(s) #출력 안됨. 이미 메모리에서 지워짐.

#decorator
print('decorator')
def document_info(func): #함수의 부가정보를 문서화하겠다는 decorator 함수.
    def mid_func(*args,**kwargs): #위에선 함수를 여기서는 인수를 받고 잇음.
        print('function name:',func.__name__)
        print('positional args:',args) #함수 안에서만 *
        print('keyword args:',kwargs)
        result =func(*args,*kwargs) #add_sub를 의미
        print('Result:',result)
        return result
    return mid_func #closure
def squares(func):
    def mid_func(*args,**kwargs):
        result=func(*args,**kwargs) #이전의 값을 가져온다? 왜 있는거지
        return result*result
    return mid_func

@squares
@document_info
def sub_int(x,y):
    return x-y
#@의 순서 큰 상관은 없음.

print(sub_int(7,3)) #so simple we want more details.
# info_sub_int = document_info(sub_int(7,3)) #@로 대체

#recursion
def factorial_recu(n):
    '''
    재귀함수를 사용한 팩토리얼 계산 함수
    :param n:n!
    :return: 자기 자신 호출 또는 1
    '''
    if n==1:
        return 1 #End
    else:
        return factorial_recu(n-1)*n

print(factorial_recu(5))
print(factorial_recu(5))

#예외처리
try:
    # raise'쉬는 시간'
    expr = input('분모 분자 입력:').split()
    print(int(expr[0]) / int(expr[1]))
except ValueError:
    print('숫자를 입력해주세요')
except ZeroDivisionError as err:
    print(err)#에러 이름을 err로 요약해서 출력해주는 것.
    print('분모에 0이 올 수 없음')
except IndexError:
    print('입력값에 예외 발생.')
finally:
    print('finihsed')
    #예외 발생 여부와 상관없이 부조건 실행.

cnt=0
def get_odds():
    for num in range(10):
        if num%2==1:
            yield num
odds=get_odds()

for i in odds:
    cnt+=1
    if cnt==3:
        print(i)

cnt=1
get_odd=(odd for odd in range(10) if odd%2==1)
for i in get_odd:
    cnt+=1
    if cnt==3:
        print(i)

groups = {
    '빅뱅':['지디','태양','탑','대성','승리'],
    '마마무':['문별','솔라','휘인','화사']
}

for group,members in groups.items():
    print(f'{group}의 멤버')
    for member in members:
        if '승리'!=member:
            print(member)


class Pokemon:
    def __init__(self, name,owner,skills): #객체 생성시 동작.
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')
        print(f'pokemon {name} created')

    def info(self):
        #self.하면 현재 객체의 ~~속성이라는 의미
        print(f'{self.owner}의 포켓몬은 {self.name}입니다.')
        for skill in self.skills:
            print(skill)


p1 = Pokemon('pikachu','한지우','50만 볼트/100만 볼트/번개')
p2 = Pokemon('turtle','오바람','고속스핀/거품/몸통박치기/하이드로펌프')

p1.info()
p2.info()

class Pikachu(Pokemon): #inheritance
    pass

pi1 = Pikachu('피카츄','덴트','번개')
pi1.info()
