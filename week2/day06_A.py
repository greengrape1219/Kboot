#9.3
def deco(func):
    def mid(*arg):
        print('start')
        func(*arg)
        print('end')
    return mid

#중간에 클로저 함수가 없으면 안될까? nontype이라고 뜨면서 안되는 것 같기도 하고.

@deco
def my_func(a):
    print(a**2)

# deco(my_func())
my_func(2)

#9.4

class OopsException(Exception):
    pass

try:
    raise OopsException('..panic...')
except OopsException as exc:
    print('Caught an Oops',exc)

# a=int(input('number?'))
# if a<1:
#     raise OopsException()
#
# try:
#     raise OopsException('panic')
# except OopsException:
#     print('Caught an Oops')

