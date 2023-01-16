#5-4

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

#143p 2번, 3번