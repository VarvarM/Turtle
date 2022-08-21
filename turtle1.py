from turtle import *

#1 красивые квадраты
def square(side):
    shape('turtle')
    for l in range(2):
        for q in range(4):
            for i in range(4):
                fd(side)
                left(90)
            left(90)
        left(45)

    done()


a = int(input())
square(a)


##################################################################
#2 соты
def hexagon(side):
    shape('turtle')
    for q in range(6):
        fd(side)
        left(60)
        for w in range(6):
            fd(side)
            right(60)
    done()


a = 80
hexagon(a)


##################################################################
#3 красивые ромбы
def romb(side):
    for q in range(10):
        for i in range(2):
            fd(side)
            left(60)
            fd(side)
            left(120)
        left(36)
    done()


a = 100
romb(a)


##################################################################
#4 звезда
def star(side):
    for i in range(5):
        fd(side)
        right(144)
    done()


star(100)


##################################################################
#5 узор с квадратами
def uzor(side):
    for i in range(20):
        for q in range(4):
            fd(side)
            left(90)
        side += 10
    done()


uzor(50)


##################################################################
#6 часы
shape('turtle')
stamp()
n = 12
angle = 360/n
ht()
penup()
for i in range(n):
    fd(100)
    pendown()
    fd(30)
    penup()
    fd(15)
    stamp()
    bk(145)
    left(angle)
done()


##################################################################
#7 спираль
ht()
shape('turtle')
penup()
a = 7
for i in range(50):
    stamp()
    right(35)
    fd(a)
    a += 2
done()


##################################################################
#8 шестиугольники разного цвета
si = 2
a = ['yellow', 'green', 'purple', 'orange', 'red', 'blue']
qq = 10
ind = 0
for i in range(50):
    pensize(si)
    if ind < 6:
        pencolor(a[ind])
    else:
        ind = 0
        pencolor(a[ind])
    fd(qq)
    left(45)
    pensize()
    si += 0.5
    qq += 3
    ind += 1
done()


##################################################################
#9 рандомные круги
import turtle # в коммах увидел
from random import *
turtle.speed(0)
turtle.Screen().colormode(255)
turtle.Screen().bgcolor('black')
turtle.hideturtle()
turtle.penup()
for i in range(800):
    q = randrange(2)
    if q:
        turtle.pendown()
    else:
        turtle.penup()
        turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle.pensize(randint(1, 10))
        turtle.goto(randint(-300, 300), randint(-300, 300))
    if not q:
        turtle.dot()
turtle.done()


##################################################################
#10 олимпиада
a = ['yellow', 'lightgreen', 'cyan', 'black', 'red']
speed(0)
ind = 0
pensize(7)
for i in range(2):
    color(a[ind])
    circle(60)
    up()
    fd(125)
    down()
    ind += 1
up()
goto(-60, 80)
down()
for i in range(3):
    color(a[ind])
    circle(60)
    up()
    fd(125)
    down()
    ind += 1
done()


##################################################################
#11 мишка фреде
pensize(2)
speed(0)
circle(20)
rt(90)
fd(80)
up()
fd(30)
down()
lt(90)
circle(90)

up()
goto(90, 40)
dot(25)
goto(-90, 40)
dot(25)

goto(0, -110)
down()
circle(140)

up()
goto(111, 131)
down()
circle(40)

up()
goto(-111, 131)
down()
circle(40)

ht()
done()


##################################################################
#12 падающие снежинки
from random import *

c = ['blue', 'purple', 'cyan', 'pink', 'aquamarine3', 'CornflowerBlue', 'PaleTurquoise3', 'snow2']
pensize(3)
speed(0)

Screen().setup(650, 650)
Screen().bgcolor('LightCyan1')


def sneg(size):
    color(choice(c))
    ch = size / 4
    for i in range(8):
        fd(size)
        for u in range(3):
            bk(ch)
            lt(45)
            fd(ch)
            bk(ch)
            rt(90)
            fd(ch)
            bk(ch)
            lt(45)
        bk(ch)
        lt(45)



for q in range(10):
    up()
    goto(randint(-300, 300), randint(-300, 300))
    down()
    raz = randrange(24, 144, 4)
    sneg(raz)
done()


##################################################################
#13 движение по стрелкам
import turtle

speed = 5


def move_up():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y + speed)


def move_down():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x, y - speed)


def move_left():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x - speed, y)


def move_right():  # функция обратного вызова
    x, y = turtle.pos()
    turtle.setposition(x + speed, y)


def change():  # функция обратного вызова
    if turtle.isvisible():
        turtle.up()
        turtle.hideturtle()
    else:
        turtle.down()
        turtle.showturtle()


def speed_increase():  # функция обратного вызова
    global speed
    speed += 1


def speed_decrease():  # функция обратного вызова
    global speed
    speed -= 1


turtle.showturtle()  # отображаем черепашку
turtle.pensize(3)  # устанавливаем размер пера
turtle.Screen().listen()  # устанавливаем фокус на экран черепашки

turtle.Screen().onkey(move_up, 'Up')  # регистрируем функцию на нажатие клавиши наверх
turtle.Screen().onkey(move_down, 'Down')  # регистрируем функцию на нажатие клавиши вниз
turtle.Screen().onkey(move_left, 'Left')  # регистрируем функцию на нажатие клавиши налево
turtle.Screen().onkey(move_right, 'Right')  # регистрируем функцию на нажатие клавиши направо
turtle.Screen().onkey(change, 'space')
turtle.Screen().onkey(speed_increase, 'q')
turtle.Screen().onkey(speed_decrease, 'w')
turtle.done()


##################################################################
#14 круги по нажатию мышки
import turtle
from random import randrange
from turtle import Screen

def random_color():
  return randrange(256), randrange(256), randrange(256)

def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    screen = Screen()
    screen.colormode(255)
    color = random_color()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.speed(0)

def left_mouse_click(x, y):
    draw_circle(x, y, 10)

turtle.hideturtle()

turtle.Screen().onclick(left_mouse_click)
turtle.Screen().listen()
turtle.done()


##################################################################
#15 домик
from turtle import *
fillcolor('blue')
speed(0)
begin_fill()
for i in range(4):
    fd(100)
    rt(90)
end_fill()

fillcolor('brown')
begin_fill()
bk(25)
for i in range(3):
    fd(150)
    lt(120)
end_fill()

done()


##################################################################
#16 светофор
from turtle import *

setpos(-40, -40)
fillcolor('black')
begin_fill()
for i in range(2):
    fd(70)
    lt(90)
    fd(200)
    lt(90)
end_fill()

kr = Turtle()
jl = Turtle()
ze = Turtle()
a = [kr, jl, ze]
colors = ['red', 'yellow', 'green']
ind = 0
yk = 100
ht()

for i in a:
    i.penup()
    i.goto(-5, yk)
    i.pd()
    i.fillcolor(colors[ind])
    i.begin_fill()
    i.circle(25)
    i.end_fill()
    ind += 1
    yk -= 60
    i.ht()
done()


##################################################################
#17 два треугольника с точками
from turtle import *
for i in range(3):
    fd(100)
    lt(120)
pu()
goto(50, -30)
pd()
lt(60)
for i in range(3):
    color('black')
    dot(20)
    fd(100)
    lt(120)
fillcolor('white')
color('white')
begin_fill()
for i in range(3):
    fd(100)
    lt(120)
end_fill()
ht()
done()


##################################################################
#18 радуждный круг
from turtle import *

a = ['red', 'orange', 'yellow', 'green', 'cyan', 'lightblue', 'blue', 'darkblue', 'purple', 'pink']
qq = 300
for i in range(10):
    color(a[i])
    dot(qq)
    qq -= 30
done()


##################################################################
#19 месяц
from turtle import *

bgcolor('blue')
color('yellow')
dot(100)
fd(20)
color('blue')
dot(100)
done()


##################################################################
#20 фазы луны из коммов
import turtle

turtle.Screen().bgcolor('DarkBlue')
turtle.hideturtle()
turtle.pencolor('orange')
turtle.dot(200)

while True:
  da = turtle.Turtle()
  da.hideturtle()
  da.pencolor('DarkBlue')
  for i in range(200, -201, -1):
    da.penup()
    da.goto(i, 0)
    da.dot(200)
    turtle.Screen().tracer(8, 0)
    da.clear()
    da.dot(200)


##################################################################
#21 рандомные звёзды
from turtle import *
from random import *

c = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink', 'aquamarine']
screensize(600, 600)
speed(0)
for i in range(200):
  pu()
  goto(randint(-290, 290), randint(-290, 290))
  lt(randrange(359))
  pd()
  size = randrange(100)
  cv = choice(c)
  color(cv)
  fillcolor(cv)
  begin_fill()
  for k in range(5):
    fd(size)
    lt(144)
  end_fill()

done()


##################################################################
#22 многоугольники из коммов
import turtle as t
import math as m
import random as r

t.colormode(255)

def figure(n, square):
    size = (square * 4 * m.tan(m.radians(180 / n)) / n) ** 0.5
    color = tuple((r.randint(0, 255) for _ in range(3)))
    t.fillcolor(color)
    t.begin_fill()

    t.forward(size / 2)
    t.left(360 / n)
    for i in range(n - 1):
        t.forward(size)
        t.left(360 / n)
    t.forward(size / 2)
    t.end_fill()


def main():
    t.speed(0)
    t.hideturtle()
    for y in range(130, -200, -75):
        for x in range(-150, 170, 75):
            t.penup()
            t.goto(x, y)
            t.pendown()
            figure(r.randint(3, 6), 1800)


main()
t.done()


##################################################################
#23 шахматная доска
from turtle import *

shape('square')
pensize(5)
speed(0)
ht()
shapesize(2)
pol = -100
for i in range(8):
    pu()
    goto(-80, pol)
    pd()
    for j in range(8):
        color('white')
        if (j + i) % 2 == 0:
            color('black')
        stamp()
        pu()
        fd(40)
    pol += 40

pu()
goto(-100, -120)
pd()

for i in range(4):
    fd(320)
    lt(90)

done()


##################################################################
#24 компас
from turtle import *

speed(0)
ht()
pensize(2)
circle(50)
pu()
goto(0, 50)
pd()
a = ['Восток', 'Запад', 'Север', 'Юг']
pp = 0
for i in range(2):
    fd(200)
    write(a[pp], align='center')
    pp += 1
    pu()
    bk(430)
    write(a[pp])
    fd(30)
    pd()
    pp += 1
    fd(200)
    lt(90)

done()


##################################################################
#25 планеты
from turtle import *

texts = ['Солнце', 'Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун', 'Плутон']
colors = ['yellow', 'goldenrod2', 'goldenrod2', 'LightBlue1', 'red', 'goldenrod2', 'goldenrod2', 'DodgerBlue3', 'DodgerBlue3', 'goldenrod2']
sizes = [50, 10, 20, 12, 8, 35, 30, 25, 25, 5, 10]
ht()
bgcolor('NavyBlue')
speed(0)
pu()
xk = 0

for i in range(10):
    goto(xk, 0)
    seth(0)
    color(colors[i])
    dot(sizes[i]*2)
    if i == 6:
        color('black')
        bk(sizes[i])
        dot(5)
        for o in range(6):
            fd(10)
            dot(5)
    goto(xk, 0)
    rt(90)
    if sizes[i] < 25:
        fd(35)
    else:
        fd(65)
    color('black')
    write(texts[i], align='center')
    xk = xk + sizes[i]+ sizes[i+1] + 25

done()


##################################################################
#26 знак стоп
from turtle import *

pensize(5)
speed(0)
ht()
for i in range(8):
    fd(80)
    lt(45)
goto(3, 5)
color('white')
fillcolor('red')
begin_fill()
for i in range(8):
    fd(75)
    lt(45)
end_fill()

penup()
goto(-40, 60)
write('STOP', font=('Aerial', 45))

done()


##################################################################
#27 сердце
from turtle import *
from math import *

speed(0)
color('red')
fillcolor('red')
t = 0
x = 128*sin(t)**3
y = 8*(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t) - 5)
pu()
goto(x, y)
pd()
begin_fill()
while t <= 2 * pi:
    x = 128 * sin(t) ** 3
    y = 8 * (13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t) - 5)
    goto(x, y)
    t += 0.01
end_fill()
done()


##################################################################
#28 звёзды по нажатию мышки
from turtle import *
from random import *

Screen().bgcolor('black')
c = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink', 'aquamarine']
speed(0)
ht()


def star(x, y):
    size = randrange(100)
    cv = choice(c)
    color(cv)
    fillcolor(cv)
    begin_fill()

    pu()
    goto(x, y)
    lt(randrange(359))
    pd()
    for k in range(5):
        fd(size)
        lt(144)
    end_fill()


def left_mouse_click(x, y):
    star(x, y)


Screen().onclick(left_mouse_click)
listen()
done()
