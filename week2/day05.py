#function : prime number

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


start = int(input("input start number : "))
end = int(input("input end number : "))
if end < start:
    start, end = end, start

for i in range(start, end + 1):
    if isprime(i):
        print(i,end=' ')

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



def do_nothing():
    pass

do_nothing()
print(do_nothing())
