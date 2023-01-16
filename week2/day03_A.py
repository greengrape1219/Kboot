#5-4,5

salutation='Mr'
name='john'
product='cleaner'
verbed='misshipped'
room='bathroom'
animals='cat'
amount='a lot'
percent='100%'
spokesman='yubin'
job_title='CEO'

letter='''Dear {0} {1},

 Thank you for your letter. We are sorry that our {3} {4} in your{5}. Please note that it should never be used in a {5}, especially near any{6}.

 Send us your receipt and {7} for shipping and handling. We will send you another {7} that, in our tests, is {8}% less likely to have {4}.
 
 Thank you for your support.
 Sincerely,
 {8}
 {9} '''

print(letter.format(salutation,name,product,verbed,room,animals,amount,percent,spokesman,job_title))

#5-6,7,8

# research0='''an English submarine 이름은 (Boaty McBoatface)로 지어졌다.
# an Australian racehorse 이름은 (Horsey McHorseface)로 지어졌다.
# an Swedish train 이름은 (Trainy McTrainface)로 지어졌다. '''

print('''%sy Mc%sface
%sy Mc%sface
%sy Mc%sface''' % ('boat'.capitalize(),'boat'.capitalize(),'gourd'.capitalize(),'gourd'.capitalize(),'spitz'.capitalize(),'spitz'.capitalize()))

print('''{0}y Mc{0}face
{1}y Mc{1}face
{2}y Mc{2}face''' .format('boat'.capitalize(),'gourd'.capitalize(),'spitz'.capitalize()))

print(f'''{'boat'.capitalize()}y Mc{'boat'.capitalize()}face
{'gourd'.capitalize()}y Mc{'gourd'.capitalize()}face
{'spitz'.capitalize()}y Mc{'spitz'.capitalize()}face''')

#6-2
guess_me=7
number=1

while True:
    if number>guess_me:
        print('oops')
        break
    elif number<guess_me:
        print('too low')
    else:
        print('found it!')
        break
    number+=1

