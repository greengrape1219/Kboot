print("I'm a\tboy")

# army = '''우리는 국가와 국민에 충성을 다하는 대한민국 육군이다.
# 하나 우리는 자유민주주의를 수호하며 조국 통일의 역군이 된다'''

army = '우리는 국가와 국민에 충성을 다하는 대한민국 육군이다.\t하나 우리는 자유민주주의를 수호하며 조국 통일의 역군이 된다'
print(army)

start = '나 ' * 4 + '\n'
middle = '헤이 ' * 3 + '\n'
end = '안녕.'
print(start + start + middle + end)

subjects = ' $ python, data structure, database    $$$'
print(subjects.title())
print(subjects.count('data'))
print(subjects.rfind('data'), subjects.rindex('data'))
print(subjects.find('data'), subjects.index('data'))
print(subjects.find('inha'))  # -1 return
# print(subjects.index('inha'))  # Exception!

subjects = ' $ python, data structure, database    $$$'
print(subjects.strip('$'))

inha = 'a duck goes into a sea'
print(inha.replace('a', 'a nice'))

pokemons_list = ['피카츄', '꼬부기', '이상해', '파이리']
pokemons_string = '/'.join(pokemons_list)
print(pokemons_string)

univ = 'Inha University'
print(univ.split())

# print(len(univ))
# print(univ[-10:-6])
# print(univ[5:-6])
# print(univ[::2])
# print(univ[5:])
# print(univ[5:15])
# print(univ[-10:])

song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
idx = song.find('m')
print(idx, song[idx].upper())

print("My kitty cat likes %s,\nMy kitty cat likes %s,\nMy kitty cat fell on his %s\nAnd now thinks he's a %s." % (
    'roast beef', 'ham', 'head', 'clam'))

questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]
print(f'Q:{questions[0]}')
print(f'A:{answers[0]}')
print(f'Q:{questions[1]}')
print(f'A:{answers[1]}')
print(f'Q:{questions[2]}')
print(f'A:{answers[2]}')

song_list = song.split()
print(song_list)
song_list[14] = song_list[14].title()
song_string = ' '.join(song_list)
print(song_string)

# idx = song.rfind('m')
# song = song.replace(song[idx], song[idx].upper())
# print(song.endswith('moray!'))


# for

while True:
    dan = int(input('Dan (0 to quit): '))

    if dan == 0:  # exit
        break
    if 1 < dan < 10:  # if dan >= 2 and dan <= 9:
        for i in range(1, 10):
            print('{0} * {1} = {2}'.format(dan, i, dan * i))
    else:
        print('2에서 9사이의 값을 입력 하세요')

# prime number v0.1

number = int(input("input number : "))
counts = 0

k = 1
while k <= number:
    if number % k == 0:
        counts = counts + 1
    k = k + 1
if counts == 2:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number.')

# prime number v0.2

number = int(input("input number : "))
counts = 0

for k in range(1, number+1):
    if number % k == 0:
        counts = counts + 1

if counts == 2:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number.')

# prime number v0.3
number = int(input("input number : "))
counts = 0

for k in range(2, number):
    if number % k == 0:
        counts = counts + 1

if counts:
    print(f'{number} is NOT prime number.')
else:
    print(f'{number} is prime number!')


# prime number v0.4

number = int(input("input number : "))
is_prime = True

for k in range(2, number):
    if number % k == 0:
        is_prime = False

if is_prime:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number.')



# prime number v0.6

number = int(input("input number : "))
is_prime = True

for k in range(2, number):
    if number % k == 0:
        is_prime = False
        break
    print(k)

if is_prime:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number.')

# prime number

start = int(input("input start number : "))
end = int(input("input end number : "))

if end < start:
    start, end = end, start

for i in range(start, end+1):
    # is_prime = True
    if i <= 1:
        continue
    for k in range(2, i):
        if i % k == 0:
            # is_prime = False
            break
    else:
        print(i, end=' ')

