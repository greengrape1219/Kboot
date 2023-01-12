#dictionary 예제

subjects = {'의사소통 영어': 'A+',
            '오래된 미래': ' B+',
            '양자역학' : 'A0'
}

student = '김도훈'
subject='오래된 미래'
print(f'{student}학생의 {subject} 과목 성적은 {subjects[subject]}입니다.') #modern스타일 포맷 함수