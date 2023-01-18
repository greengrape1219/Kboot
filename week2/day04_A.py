#7.1
year=2001
years_list=[ year+i for i in range(6)]
print(years_list)

#7.2
print(years_list[3])

#7.3
print(years_list[-1])

#7.4
things=['mozzarella','cinderella','salmonella']

#7.5
things[1].capitalize()

#7.6
things[0].upper()

#7.7
things.pop()
print(things)

#7.8
surprise=['Groucho','Chico','Harpo']

#7.9
surprise[2]=surprise[2].lower()
surprise[2]=surprise[2][::-1].title()
print(surprise)

#7.10

even=[number for number in range(10) if number%2==0]
print(even)

#7.11
start1= ['fee','fie','foe']
rhymes=[
    ('flop','get a mop'),
    ('fope','turn the rope'),
    ('fa','get your ma'),
    ('fat','pet the cat'),
    ('fog','walk the dog'),
    ('fun',"say we're done"),
]
start2='Someone better'

for k in rhymes:
    for i in start1:
        print(i.title()+'! ', end='')
    print(k[0].title()+'!')
    print(start2+' '+k[1]+'.')

#8.1
e2f={'dog':'chien','cat':'chat','walrus':'morse'}

#8.2
print(e2f['walrus'])

#8.3
f2e={}
for key,value in e2f.items():
    f2e[value]=key
print(f2e)

#8.4
for item,value in e2f.items():
    if value=='chien':
        print(item)

#8.5
for i in e2f.keys():
    print(i)

#8.6
life={'animals':{'cats':'Henri','octopi':'Grumpy','emus':'Lucy'},
      'plants':{},
      'other':{}}

#8.7
print(life.keys())

#8.8
print(life['animals'].keys())

#8.9
print(life['animals']['cats'])

#8.10
squares={ number:number**2 for number in range(10)}
print(squares)
