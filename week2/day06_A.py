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


#10.1
class Thing():
    pass

example=Thing()

print(Thing,example)

#10.2
class Thing2():
    def __init__(self,letters):
        self.letters=letters

print(Thing2('abc'))

#10.3
class Thing3():
    def __init__(self,letters):
        self.letters=letters
Ti=Thing3('xyz')
print(Ti)

#10.4
class Element():
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number

    def dump(self):
        print(f'name is {self.name}, symbol is {self.symbol},number is {self.number}')
E1=Element('Hydrogen','H','1')
print(E1)

#10.5
el_dict={'name':'Hydrogen','symbol':'H','number':1}
hydrogen=Element(el_dict['name'],el_dict['symbol'],el_dict['number'])
print(hydrogen)

#10.6
hydrogen.dump()

#10.7
print(hydrogen)