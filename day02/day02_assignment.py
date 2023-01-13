#과제 리포지토리 만들어서 커밋 두번 파일 하나 있어야함. day02_mision 클래스룸에 깃헙 링크

from random import *
secret= randint(1,10)
guess= randint(1,10)

if secret-guess>0:
    print('too low')
elif secret-guess<0:
    print('too high')
else:
    print('just right')

small=True
green=True

if small:
    if green:
        print('완두콩은 작고 초록색이다.')
    else:
        print('체리는 작고 초록색이 아니다.')
else:
    if green:
        print('수박은 크고 초록색이다.')
    else:
        print('호박는 크고 초록색이 아니다.')

