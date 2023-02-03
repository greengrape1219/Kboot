pokemons = []  # 빈 배열


# 함수를 이용한 데이터 삽입
def add_data(pokemon):
    '''
    선형 리스트의 맨 뒤에 원소 삽입
    :param pokemon: pokemon list
    :return:
    '''
    pokemons.append(None)
    # pokemons[len(pokemons) - 1] = pokemon
    pokemons[-1] = pokemon
    # 파이썬은 -1 역방향 인덱스를 지원하기 때문에 위의 코드는 이렇게 대체 가능.


add_data('피카츄')
add_data('파이리')
add_data('꼬부기')
add_data('라이츄')
add_data('이상해')

print(pokemons)

pokemons = ["피카츄", "라이츄", "파이리", "꼬북이", "이상해"]


# 포문을 이용한 데이터 삽입
def insert_data(position, pokemon):
    '''
    선형 리스트의 idx위치에 원소 삽입
    :param position: int
    :param pokemon: str
    :return:
    '''
    if position < 0 or position > len(pokemons):
        print("Out of range.")
        return

    pokemons.append(None)  # 빈칸 추가
    # kLen = len(pokemons)  # 배열의 현재 크기

    for i in range(len(pokemons) - 1, position, -1):
        pokemons[i] = pokemons[i - 1]
        # 3의 자리에 있는 값을 4의 자리로 옮긴다는 의미
        pokemons[i - 1] = None

    pokemons[position] = pokemon  # 지정한 위치에 친구 추가


print(pokemons)
insert_data(2, '거북왕')
print(pokemons)
insert_data(3, '어니부기')
insert_data(6, '가부키')  # 인덱스 6  out of range 앞에 값추가해줘서 늘어났기때문에 안난다.
print(pokemons)

# pokemons.insert(3,'어니부기')
# 위의 코드와 같이 간단한 코드로 구현할 수 있지만 내부 프로그램이 어떻게 돌아하는지 구현해본 것이다.


# 데이터 삭제
pokemons = ["피카츄", "라이츄", "파이리", "꼬북이", "이상해"]


def delete_data(idx):
    '''
    선형 리스트 idx의 원소 삭제
    :param idx: int
    :return: void
    '''
    if idx < 0 or idx > len(pokemons):
        print("Out of range.")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None  # 데이터 삭제

    for i in range(idx + 1, len_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None  # 배열의 맨 마지막 위치 삭제

    del (pokemons[len_pokemons - 1])
    # pokemons.pop() #두개 다 쓰면 인덱스 에러난다 왜..?


if __name__ == "__main__":
    # 자바의 메인함수?
    delete_data(1)
    print(pokemons)
    delete_data(3)
    print(pokemons)

# 코드 수정 퀴즈
katok = ['다현', '정연', '쯔위', '사나', '지효']


def delete_data2(position):
    if position < 0 or position > len(katok):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    kLen = len(katok)
    katok[position] = None  # 데이터 삭제

    for i in range(position + 1, kLen):
        # del pokemons[i] #index out of range 오류
        katok[i] = None  # ['다현',none,none] 이라고 뜸.

        # katok[i - 1] = katok[i]
        # katok[i] = None  # 배열의 맨 마지막 위치 삭제

    # del (katok[kLen - 1])

    for i in range(position, 5):
        katok.pop()


delete_data2(1)
print(katok)


# delete_data(3)
# print(katok)


## 함수 선언 부분 ##
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen - 1] = friend


def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)  # 빈칸 추가
    kLen = len(katok)  # 배열의 현재 크기

    for i in range(kLen - 1, position, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None

    katok[position] = friend  # 배열의 제일 뒤에 친구 추가


def delete_data(position):
    if position < 0 or position > len(katok):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    kLen = len(katok)
    katok[position] = None  # 데이터 삭제

    for i in range(position + 1, kLen):
        katok[i - 1] = katok[i]
        katok[i] = None  # 배열의 제일 위치 삭제

    del (katok[kLen - 1])


## 전역 변수 선언 부분 ##
katok = []
menu = -1  # 1: 추가, 2: 삽입, 3: 삭제, 4: 종료

## 메인 코드 부분 ##
if __name__ == "__main__":

    while True:  # (select != 4): #괄호 없애주고
        menu = input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> ")
        if (menu == '1'):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(katok)
        elif (menu == '2'):
            pos = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(pos, data)
            print(katok)
        elif (menu == '3'):
            pos = int(input("삭제할 위치--> "))
            delete_data(pos)
            print(katok)
        elif (menu == '4'):
            print(katok)
            # exit #그자리에서 멈추는거
            break  # 그 뒤의 코드가있으면 그것까지 실행.
            # 괄호 안에 문자열 입력해도 오류나지않게 숫자 ''로 바꿔주기
            # 그럼 문자를 입력해도 에러나지 않음 대신 int()함수 써준거 없애야함!!
        else:
            print("메뉴 1~4 중 하나를 입력하세요.")
            continue


    # 예제
    # friends=[('다현',200),('정연',150),('쯔위',90),('사나',30),('지효',15)]
    def find_data(friend, k_count):
        idx = 0


    friend = input("추가할 친구--> ")
    cnt = input('삽입할 위치-->')


# if __name__ == "__main__":


## 함수 선언 부분 ##
def printPoly(p_x):
    '''
    다항식을 포맷에 맞게 출력하는 함수
    :param p_x: 다항식의 계수를 원소로 가지고 있는 list
    :return: 다항식 str
    '''
    term = len(p_x) - 1  # 최고차항 숫자 = 배열길이-1 최고차항 항 4개면 3
    polyStr = "P(x) = "

    for i in range(len(px)):
        coef = p_x[i]  # 계수 분리
        # if coef >= 0:
        #     poly_str = poly_str + "+"

        if coef == 0:
            term -= 1
            continue
        elif (coef >= 0) and i > 0:  # 제일 앞의 항은 +를 생략하는 코드
            polyStr += "+"
        else:
            polyStr += "-"

        polyStr += str(coef) + "x^" + str(term) + " "
        term -= 1  # 차수를 하나씩 뺀다.

    return polyStr


def calcPoly(xValue, p_x):
    '''
    다항식의 산술연산
    :param xVal: 계수를 원소로 가지고 있는 list
    :param p_x: 다항식의 계산 결과 값 int
    :return: 
    '''
    return_Value = 0
    term = len(p_x) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = p_x[i]  # 계수
        return_Value += coef * xValue ** term
        term -= 1

    return return_Value


## 전역 변수 선언 부분 ##
px = [7, -4, 0, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0

## 메인 코드 부분 ##
if __name__ == "__main__":
    print(printPoly(px))

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, px)
    print(pxValue)


## 함수 선언 부분 ##
def printPoly(t_x, p_x):
    '''
    다항식을 포맷에 맞체 출력하는 함수.
    :param t_x: 계수를 원소로
    :param p_x: 차수를 원소로 가지고 있는list
    :return:
    '''
    polyStr = "P(x) = "

    for i in range(len(p_x)):
        term = t_x[i]  # 항 차수
        coef = p_x[i]  # 계수

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "

    return polyStr


def calcPoly(xValue, t_x, p_x):
    returnValue = 0

    for i in range(len(px)):
        term = t_x[i]  # 항 차수
        coef = p_x[i]  # 계수
        returnValue += coef * xValue ** term

    return returnValue


## 전역 변수 선언 부분 ##
tx = [300, 20, 0]
px = [7, -4, 5]

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = printPoly(tx, px)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, tx, px)
    print(pxValue)


## 함수 선언 부분 ##
def printPoly(p_x):
    '''
    다항식을 포맷에 맞체 출력하는 함수.
    :param t_x: 계수를 원소로
    :param p_x: 차수를 원소로 가지고 있는list
    :return:
    '''
    polyStr = "P(x) = "

    for i in range(len(p_x)):
        term = p_x[0][i]  # 항 차수
        coef = p_x[1][i]  # 계수

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "

    return polyStr


def calcPoly(xValue, p_x):
    returnValue = 0

    for i in range(len(px)):
        term = p_x[0][i]  # 항 차수
        coef = p_x[0][i]  # 계수
        returnValue += coef * xValue ** term

    return returnValue


# 전역 변수
tx = [[300, 20, 0], [7, -4, 5]]
printPoly(tx)
calcPoly(1, tx)


# 단순연결 리스트

## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_node(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()


## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__":

    node = Node()  # 첫 번째 노드
    node.data = dataArray[0]
    head = node #다현을 head에 입력
    memory.append(node) #memory에 올린다.

    for data in dataArray[1:]:  # 두 번째 이후 노드
        pre = node 
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    print_node(head)
