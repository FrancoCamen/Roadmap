from arbolFranco import BinaryTree
from random import randint

arbol = BinaryTree()

for i in range (20):
    arbol.insert_node(randint(0, 100))

arbol.insert_node(50)



def a_Sweep (arbol):
    type = input("Indicate the type of sweep (in-post-pre-level)")
    if type == "in":
        print("Sweep inorden: ")
        arbol.inorden()
    elif type == "post":
        print("Sweep postorden: ")
        arbol.postorden()
    elif type == "pre":
        print("Sweep preorden: ")
        arbol.preorden()
    elif type == "level":
        print("Sweep By level: ")
        arbol.by_level()

#search for a value within the tree
def b_Search(arbol):
    type = input("Enter value to search")
    result = arbol.search(int(type))
    if result:
        print("The value is in the tree")
    else:
        print("The value is not in the tree")

#Delete value
def c_Delete(arbol):
    type = input("Enter value to delete")
    result = arbol.delete_node(int(type))
    if result:
        print("Value was deleted")
    else:
        print("The value is not in the tree")

# Height of subtrees
def d_Height(arbol):
    arbol.height_subtree()

def e_Repeats(arbol):
    type = input("Enter value to see your repetitions")
    ocurrences = arbol.contar(int(type))
    if ocurrences is not None:
        print(f"The value is repeated {ocurrences} times")
    else:
        print("The value is not repeated")

e_Repeats(arbol)










