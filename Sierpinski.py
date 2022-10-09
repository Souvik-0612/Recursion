from turtle import *

def Sierpinski (length,h):
    if h == 0:
        fillcolor("Green")
        begin_fill()
        for i in range(0,3):
            fd(length)
            left(120)
        end_fill()
    else:
        Sierpinski (length/2,h-1)
        fd(length/2)
        Sierpinski (length/2,h-1)
        bk(length/2)
        left(60)
        fd(length/2)
        right(60)
        Sierpinski (length/2,h-1)
        left(60)
        bk(length/2)
        right(60)


speed(0)
penup()
goto(-500,-200)
pendown()
width(3)
Sierpinski (1000,5)
done()