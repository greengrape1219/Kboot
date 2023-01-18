#function : prime number
import random


def isprime(n):
    '''매개변수로 받은 정수가 소수인지 여부를 판정하는 함수
    :param n: integer numbet
    :return : true or false
    '''

    if n <= 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    else:
        return True
#help(isprime) #함수 앞 도움말을 준다.


def do_nothing():
    pass

do_nothing()
print(do_nothing())


start = int(input("input start number : "))
end = int(input("input end number : "))
if end < start:
    start, end = end, start

for i in range(start, end + 1):
    if isprime(i):
        print(i,end=' ')

import random as r
def calc_fee(*args):
    '''
    놀이공원 요금 계산 프로그램
    :param args: ages
    :return: 지불할 총 입장료
    '''

    total=0
    for age in args:
        if 19 <= age: #adult
            total+=10000
        else:
            total+=3000
    return total

print(calc_fee(20,20,25))
print(calc_fee(10,6,45,32))


people=int(input('몇명?'))
def generate():
    for i in range(people):
        age_list=r.randint(1,100)
    return age_list



def calc_fee_v2(args)->dict:
    #-> 타입힌트
    '''
    놀이공원 요금 계산 프로그램
    :param args: ages in list
    :return: 전체 인원 수, 어른 수, 아이 수, 지불할 총 입장료
    '''
    adults = 0
    kids = 0
    total = 0
    for age in args:
        if 19 <= age:  # adult
            total += 10000
            adults+=1
        else:
            total += 3000
            kids+=1
    return {'people_count':len(args),'adults_count':adults,'kids_count':kids,'money':total}


no_of_visitor = int(input('몇명이세요?'))
ages=[r.randint(1,60) for age in range(no_of_visitor)]
results=calc_fee_v2(ages)
print(f"총 {results['people_count']} 명 방문 하셨고 어른 {results['adults_count']} 아이{results['kids_count']} 총 {results['money']}원 입니다.")

def inha():
    '''
    숫자 출력 함수
    :return: 없음.
    '''
    print(60)

def call_func(f):
    '''
    매개 변수로 함수를 넘겨 받아 실행
    :param f: 매개 변수가 함수
    :return:
    '''

call_func(inha) #함수 안의 함수 고차원 함수

# def run_func(f,arg) 채우기

def sum_args(*args):
    return sum(args)
print(sum_args(1,2,3,4))
def run_with_positional_args(func,*args):
    return(func,*args)
    #인수 (f,1,2,3,4) 이런 식으로 적음.

def calculate():
    x=1
    y=2
    def add_sub(n):
        # nonlocal x
        # x=11
        return x+n-y
    return add_sub
#closure () 없어도 됨.

c1=calculate()
for i in range(5):
    print(c1(i))

#lambda

def process(no_lists,f):
    for no in no_lists:
        print(f(no))
# def squares(n):
#     '''
#     제곱 횟수
#     :param n: integer
#     :return: integer
#     '''
#     return n^n

numbers =r.random(1,100) for i in range(5):
print(numbers)