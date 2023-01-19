# 8.11
odd = {number for number in range(10) if number % 2 == 1}
print(odd)

# 8.12 제너레이터문제 나중에 배우고 하기!
for i in 'got':
    print(i)

for i in range(10):
    print(i)

# 8.13
a = ['optimist', 'pessimist', 'troll']
sentence = ['the glass is half full', 'the glass is half empty', 'How did you get a glass?']
print(dict(zip(a, sentence)))

# 8.14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']
print(set(zip(titles, plots)))

# 8.15
Harry_potter = ['Harry', 'Ron', 'Hermione']


def good():
    return Harry_potter


print(good())