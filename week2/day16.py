#과제코드

# def find_and_insert_data(pokemon, k_count) :
# 	findPos = -1
# 	for i in range(len(pokemons)):
# 		pair = pokemons[i]
# 		if k_count <= pair[1]:
# 			findPos = i
# 			break
# 	if findPos == -1:
# 		findPos = len(pokemons)
#
# 	insert_data(findPos, [pokemon, k_count])
#
#
# def insert_data(position, pokemon):
# 	if position < 0 or position > len(pokemons):
# 		print("데이터를 삽입할 범위를 벗어났습니다.")
# 		return
#
# 	pokemons.append(None)
# 	kLen = len(pokemons)
#
# 	for i in range(kLen - 1, position, -1):
# 		pokemons[i] = pokemons[i - 1]
# 		pokemons[i - 1] = None
#
# 	pokemons[position] = pokemon
#
#
#
# pokemons = [['피카츄', 300], ['꼬부기', 500], ['어니부기', 700], ['거북왕', 1000]]
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__":
#
# 	while True:
# 		pokemon = input("새로운 몬스터 : ")
# 		hp = int(input("체력 : "))
# 		find_and_insert_data(pokemon, hp)
# 		print(pokemons)
#딕셔너리 만들라며..?

class Node:
	def __init__(self):
		self.data = None
		self.link = None

	# def __repr__(self):
	# 	return f'포켓몬스터!'

# 자바에서 tosrting과 같다고 하신다. 그러고 파이썬에서는 매직메서드 __str__
# 자바의 최상위 클래스 object


def print_nodes(start):
    current = start
    if current == None :
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link  # 다음 노드로 이동
        print(current.data, end=' ')
    print()


memory = []
head, current, pre = None, None, None
dataArray = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]

## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self,data) :
		self.data = None
		self.link = None
        #생성자의 필드를 받아서 초기화

def printNodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def insert_nodes(find_data, insert_data) :
	global memory, head, current, pre

	if head.data == find_data :      # 첫 번째 노드 삽입
		node = Node(insert_data)
        # node.data = insert_data #위에서 생성자 파라미터로 받아서 생략 가능.
		node.link = head
		head = node
		return

	current = head
	while current.link != None :    # 중간 노드 삽입
		pre = current
		current = current.link
		if current.data == find_data :
			node = Node(insert_data)
			# node.data = insert_data
			node.link = current
			pre.link = node
			return

	node = Node(insert_data)                   # 마지막 노드 삽입
	node.data = insert_data
	current.link = node

def delete_nodes(delete_data):
    global memory, head, current, pre

    if head.data ==delete_data:
        print("첫번째 노드 삭제됨.")
        current =head
        head= head.link
        del current
        return

    current =head
    while current.link !=None:
        pre=current
        current=current.link #current 지나가는 항목
        if current.data==delete_data:
            pre.link =current.link
            print("중간 노드 삭제됨.")
            del current
            return
    print("삭제할 노드 찾지 못함.")
    #삭제할 데이터를 못찾은 경우에는 함수 종료

def find_nodes(find_data):
    global memory, head, current, pre

    current =head
    if current.data==find_data:
        return current

    while current.link!= None:
        current =current.link #슥슥 지나가는 코드.
        if current.data == find_data:
            return current

    return Node(None)

# ## 전역 변수 선언 부분 ##
# memory = []
# head, current, pre = None, None, None
# 메모리 변수 불필요하다고 교수님이 다 지우고 계심..


if __name__ == "__main__":
    node = Node(None)
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node(None)
        node.data = data
        pre.link = node
        memory.append(node)

    print_nodes(head)
    print(memory)
    # print(node.data)
    # print(pre.data)

    insert_nodes("피카츄","잠만보")
    print_nodes(head)
    insert_nodes("파이리","어니부기")
    print_nodes(head)
    insert_nodes("성윤모","거북왕") #안에 없는 항목
    print_nodes(head)

    delete_nodes("잠만보")
    print_nodes(head)
    delete_nodes("어니부기")
    print_nodes(head)
    delete_nodes("강찬석") #존재하지 않는 항목.
    print_nodes(head)

    print(find_nodes("파이리").data) #print_node하면 스타트값부터 다 나온다.
    print(find_nodes("박병석").data)
    #find_nodes(param) 이대로 쓰면 노드 객체가 출력되고 문자열은 출력 되지 않는다.
    #.data 해줘야지 데이터 값 출력됨.



## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()

def makeSimpleLinkedList(namePhone) :
	global memory, head, current, pre
	printNodes(head)

	node = Node()
	node.data = namePhone
	memory.append(node)
	if head == None :			# 첫 번째 노드일 때
		head = node
		return

	if head.data[0] > namePhone[1] :	# 첫 번째 노드보다 작을 때
		node.link = head
		head = node
		return

	# 중간 노드로 삽입하는 경우
	current = head
	while current.link != None :
		pre = current
		current = current.link
		if current.data[0] > namePhone[0]:
			pre.link = node
			node.link = current
			return

	# 삽입하는 노드가 가장 큰 경우
	current.link = node

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = [["지민", "010-1111-1111"], ["정국", "010-2222-2222"], ["뷔", "010-3333-3333"], ["슈가", "010-4444-4444"], ["진", "010-5555-5555"]]
dataArray2 = [["지민", "180"], ["정국", "181"], ["뷔", "183"], ["슈가", "178"], ["진", "190"]]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	for data in dataArray2 :
		makeSimpleLinkedList(data)

	printNodes(head)