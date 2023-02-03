# 10.1
class Thing():
    pass


example = Thing()

print(Thing, example)


# 10.2
class Thing2():
    def __init__(self, letters):
        self.letters = letters


print(Thing2('abc'))


# 10.3
class Thing3():
    def __init__(self, letters):
        self.letters = letters


Ti = Thing3('xyz')
print(Ti)


# 10.4
class Element():
    def __init__(self, input_name, symbol, number):
        self.hidden_name = input_name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f'name is {self.hidden_name}, symbol is {self.symbol},number is {self.number}')

    def __str__(self):
        return f'name is {self.hidden_name}, symbol is {self.symbol},number is {self.number}'
    #print 가 아닌 return


    @property
    def name(self):
        print('getter')
        return self.hidden_name
    @name.setter
    def name(self,input_name):
        print('setter')
        self.hidden_name=input_name





E1 = Element('Hydrogen', 'H', '1')
print(E1)

# 10.5
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
print(hydrogen)

# 10.6
# hydrogen.dump()

# 10.7
print(hydrogen)

#10.8
E1.name

#10.9
class Animals():
    def __init__(self,name,food):
        self.name=name
        self.food=food

    def eats(self):
        return f'{self.food} ({self.name})'

class Bear(Animals):
    pass
class Rabbit(Animals):
    pass

class Octothorpe(Animals):
    pass


B1=Bear('Bear','Berries')
R1=Rabbit('Rabbit','clover')
O1=Octothorpe('Octothorpe','campers')
print(B1.eats())
print(R1.eats())
print(O1.eats())

#10.10
class Machine():
    def __init__(self,name,function):
        self.name=name
        self.function=function

    def does(self):
        return f"'{self.function}'({self.name}"

class Laser(Machine):
    pass
class Claw(Machine):
    pass
class SmartPhone(Machine):
    pass

L1=Laser('Laser','disintegrate')
C1=Claw('Claw','crush')
S1=SmartPhone('SmartPhone','ring')
print(L1.does())
print(C1.does())
print(S1.does())