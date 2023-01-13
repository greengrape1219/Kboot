#chap3

number =0b10
print(number)
number =0x10
print(number)
number=0o10
print(number)

#chap04 if

limits =20
tweets ="pass"*6

if limits - len(tweets) >= 0: #len 쓰지 않으면 오류 발생.
    print(tweets)
else:
    print('제한 글자수 초과.')

diff = limits - len(tweets) #를 단축하는 방법 diff := tweet_limit -len(tweet_string) >= 0:
if diff >=0 :
    print(tweets)
else:
    print(abs(diff))

import random
limits =20
tweets ="pass"*random.randint(1,6)

if limits - len(tweets) >= 0: #len 쓰지 않으면 오류 발생.
    print(tweets)
else:
    print('제한 글자수 초과.')