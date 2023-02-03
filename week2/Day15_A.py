
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

lst=[]

def find_inset_data(pokemon, hp):
    dict = {}
    dict[pokemon]=hp
    cnt=0

    for in_poke ,values in dict.items():
        if dict[in_poke]<=dict[pokemon]:
            lst.insert(cnt,dict)
        else:
            cnt+=1
        return lst

find_inset_data("꼬부기", 20)
find_inset_data("어니부기", 50)
find_inset_data("거북왕", 100)
print(lst)

#교재코드대로
def find_and_insert_data(pokemon,hp):
    find_pos=-1
    dict = {}
    dict[pokemon] = hp
    for i in range(len(my_pokemons)):
        if hp >= my_pokemons[i][1]:
            find_pos=i
        else:
            # find_pos=-1
            find_pos=len(my_pokemons)-1
    print(find_pos)
    my_pokemons.insert[find_pos,dict]
    # insert_data(find_pos,dict)
#
# def insert_data(idx,dict):
#     my_pokemons[idx]=dict
#     return

my_pokemons=[]

if __name__=="__main__":
    while True:
        input_name=input("추가할 포켓몬?")
        input_hp=input("포켓몬의 체력?")
        find_inset_data(input_name,input_hp)
        print(my_pokemons)

