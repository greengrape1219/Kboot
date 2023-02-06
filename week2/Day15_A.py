
#P113 연습문제의 답
#1 : 선형리스트
#2 : 1
#3 : 2
#4 : katok.append(None)
#5 : katok.pop()
#6 :
# katok=[]
# def add_data(friend):
#     kLen=len(katok)
#     katok.append(None)
#     katok[kLen-1]=friend
#7 : 4
#8 : 4


lst=[{"꼬부기":20}]

def find_insert_data(pokemon, hp):
    dict = {}
    dict[pokemon]=hp

    for i in range(len(lst)):
        # print(i)
        for key,val in lst[i].items():
            if val<=hp:
                lst.insert(i, dict)
                break
            else:
                lst.append(dict)
                break
        print(lst)
        break #브레이크문 하나였더니 안쪽 포문만 빠져나와서.... 여러번 써졌다..

    # print(lst)

find_insert_data("어니부기", 50)
find_insert_data("거북왕", 100)
find_insert_data("피카츄", 10)
# find_inset_data("파이리",70)






#교재코드대로

my_pokemons = []
def find_insert_data(pokemon,hp):
    find_pos=-1
    # dict = {}
    # dict[pokemon] = hp
    for i in range(0,len(my_pokemons)):#for dict_in_pokemons in my_pokemons():
        if len(my_pokemons)==1:
            for key,val in my_pokemons[i].items(): #if hp >= my_pokemons[i].values():
                if hp>= val:
                    find_pos=i #-1 해줘야해!!! 보다 큰수 다음에 계속 저장된다.
                    break
                    # 왜 쓰는 거지? 필요없지 않나? 아 포문 계속 돌면서 pos값이 커지고 필요없는 반복이라 그렇다.
        else:
            for key,val in my_pokemons[i].items(): #if hp >= my_pokemons[i].values():
                if hp>= val:
                    find_pos=i-1 #-1 해줘야해!!! 보다 큰수 다음에 계속 저장된다.
                    break
    if find_pos==-1:
        find_pos=len(my_pokemons) #생략 가능.

    insert_data(find_pos,{pokemon:hp}) #{}안에 콤마 입력하면 dict 가 아닌 set가 생성되니 주의하자..


def insert_data(idx,dict):
    # if idx<0 or idx>len(my_pokemons): #생략 가능.
    #     return #이 범위 안에 있으면 리턴해라
    my_pokemons.append(None)
    lst_len=len(my_pokemons)

    for i in range(lst_len-1,idx,-1):
        my_pokemons[i]=my_pokemons[i-1]
        my_pokemons[i-1]=None

    my_pokemons[idx]=dict
    return


if __name__=="__main__":
    while True:
        input_name=input("추가할 포켓몬?")
        input_hp=int(input("포켓몬의 체력?")) #int 빼먹지마!
        find_insert_data(input_name,input_hp)
        print(my_pokemons)

