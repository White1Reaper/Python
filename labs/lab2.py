# Тангиев Руслан, 37/1

# Лабораторная работа №2.

# задание 1. Вариант 2.Даны два списка чисел. Посчитайте, сколько чисел содержится 
# одновременно как в первом списке, так и во втором.
def find_ident_el():
    x = input("Введите число в список a: ")
    a = []
    while (x != ""):
        if x.isdigit():
            a.append(int(x))
        else:
            print("Неверный ввод!")
        x = input("Введите число в список а: ")

    b=[]
    x = input("Введите число в список b: ")
    while (x != ""):
        if x.isdigit():
            b.append(int(x))
        else:
            print("Неверный ввод!")
        x = input("Введите число в список b: ")
    for i in a:
        for j in b:
            if(i==j):
                print(i)
                break

# Задание 2. Вариант 12
# Даны два элемента в дереве. Определите, является ли один из них
# потомком другого.
# Во входных данных записано дерево в том же формате, что и в
# предыдущей задаче Далее идет число запросов K.
# В каждой из следующих K строк, содержатся имена двух элементов дерева.
# Для каждого такого запроса выведите одно из трех чисел: 1, если первый
# элемент является предком второго, 2, если второй является предком первого
# или 0, если ни один из них не является предком другого.
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None


def add_child(parent, child_name):
    child = Node(child_name)
    child.parent = parent
    parent.children.append(child)

def get_level(node, target, level=0):
    if node.data == target:
        return level
    for child in node.children:
        level_found = get_level(child, target, level + 1)
        if level_found is not None:
            return level_found
    return None

def find_element(node, element):
    if node.data == element:
        return node

    for child in node.children:
        found_element = find_element(child, element)
        if found_element is not None:
            return found_element

    return None


def tree():

    oldest_ancestors = []
    n = int(input("Введите кол-во пар: "))
    person, ans = map(str, input("Введите имя члена и его предка: ").split())
    ans1 = Node(ans)
    add_child(ans1, person)
    oldest_ancestors.append(ans1)
    for i in range(n-1):
        person, ans = map(str, input("Введите имя члена и его предка: ").split())
        if find_element(oldest_ancestors[0], ans) is not None:
            ans1 = find_element(oldest_ancestors[0], ans)
            add_child(ans1, person)
        else:
            ans1 = Node(ans)
            add_child(ans1, person)
            oldest_ancestors.append(ans1)
    n = int(input("Введите кол-во проверяемых пар: "))
    for i in range(n):
        a, b = map(str, input("Введите имена 2 членов: ").split())
        is_ancestor = False
        for ancestor in oldest_ancestors:
            if find_element(ancestor, a) is not None and find_element(ancestor, b) is not None:
                is_ancestor = True
                break
        if (is_ancestor and (get_level(ancestor,a)<get_level(ancestor,b))):
            print("1")
        else:
            is_ancestor = False
            for ancestor in oldest_ancestors:
                if find_element(ancestor, b) is not None and find_element(ancestor, a) is not None:
                    is_ancestor = True
                    break
            if is_ancestor:
                print("2")
            else:
                print("0")

tree()
