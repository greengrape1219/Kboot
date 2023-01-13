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