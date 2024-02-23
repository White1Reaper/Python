# Тангиев Руслан, 37/1

# Лабораторная работа №3.

# Эадание 1. Вариант 12. Написать программу, демонстрирующую работу с объектами
# двух типов T1 и T2, для чего создать систему соответствующих классов.
# Каждый объект должен иметь идентификатор (в виде произвольной строки
# символов) и одно или несколько полей для хранения состояния (текущего
# значения) объекта
# объекты: triangle, pentagon
# методы: is_intersect, compare
# Задание 2. Необходимо предусмотреть генерацию и обработку
# исключений для возможных ошибочных ситуаций
class Point:
    def __init__(self, x,y):
        self.x = float(x)
        self.y = float(y)
class Pentagon:
    def __init__(self,points):
        self.points = points
class Triangle:
    def __init__(self,points):
        self.points = points
def define_triangle():
    points_of_triangele=[]
    while len(points_of_triangele)<3:
        try:
            x, y = map(str, input("Введите координаты вершины треугольника (x,y): ").split())
            try:
                float(x)
                try:
                    float(y)
                    point=Point(float(x), float(y))
                    points_of_triangele.append(point)
                except ValueError:
                    print("Неверный ввод координаты y!")
            except ValueError:
                print("Неверный ввод координаты х!")
        except ValueError:
            print("Необходимо ввести ровно 2 значения через пробел!")
    return Triangle(points_of_triangele)
def define_pentagon():
    points_of_pentagon = []
    while len(points_of_pentagon) < 5:
        try:
            x, y = map(str, input("Введите координаты вершины треугольника (x,y): ").split())
            try:
                float(x)
                try:
                    float(y)
                    point = Point(float(x), float(y))
                    points_of_pentagon.append(point)
                except ValueError:
                    print("Неверный ввод координаты y!")
            except ValueError:
                print("Неверный ввод координаты х!")
        except ValueError:
            print("Необходимо ввести ровно 2 значения через пробел!")
    return Pentagon(points_of_pentagon)
def det(point1,point2):
    return point1.x*point2.y-point1.y*point2.x
def S_of_figure(figure):
    sum_det=0
    for counter in range(len(figure.points)):
        if counter<len(figure.points)-1:
            sum_det+=det(figure.points[counter],figure.points[counter+1])
        else:
            sum_det+=det(figure.points[counter],figure.points[0])
    return sum_det/2
def compare(triangle, pentagon):
    if S_of_figure(triangle)>S_of_figure(pentagon):
        print("площадь треугольника больше площади пятиугольника")
    elif S_of_figure(triangle)<S_of_figure(pentagon):
        print("площадь пятиугольника больше площади треугольника")
    else:
        print("площади равны")
def is_intersect(triangle,pentagon):
    xmax1= triangle.points[0].x
    xmin1= triangle.points[0].x
    ymax1 = triangle.points[0].y
    ymin1 = triangle.points[0].y
    xmax2 = pentagon.points[0].x
    xmin2 = pentagon.points[0].x
    ymax2 = pentagon.points[0].y
    ymin2 = pentagon.points[0].y
    check=0
    for i in triangle.points:
        if xmax1<i.x:
            xmax1=i.x
        if xmin1>i.x:
            xmin1=i.x
        if ymax1<i.y:
            ymax1=i.y
        if ymin1>i.y:
            ymax1=i.y
    for i in pentagon.points:
        if xmax2<i.x:
            xmax2=i.x
        if xmin2>i.x:
            xmin2=i.x
        if ymax2<i.y:
            ymax2=i.y
        if ymin2>i.y:
            ymin2=i.y
    if xmax1<=xmax2 and xmin1>=xmin2 and ymax1<=ymax2 and ymin1>=ymin2:
        print(" Треугольник внутри пятиугольника")
        check=1
    if xmax2<=xmax1 and xmin2>=xmin1 and ymax2 <= ymax1 and ymin2 >= ymin1 and not check:
        print(" Пятиугольник внутри треугольника")
        check=1
    if not check:
        print("ни одна из фигур не лежит внутри другой")
def work_with_objects():
    triangle=define_triangle()
    pentagon=define_pentagon()
    is_intersect(triangle,pentagon)
    compare(triangle,pentagon)

work_with_objects()

