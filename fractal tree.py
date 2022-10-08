from turtle import *
def fractal_tree(L):
	if L < 1:
		return
	else:
		fd(L)
		lt(30)
		fractal_tree(L*f)
		rt(60)
		fractal_tree(L*f)
		lt(30)
		bk(L)
		
color("Green")
width(4)
speed(0)		
penup()
goto(0, -200)
pendown()
lt(90)
f = 0.5
fractal_tree(500)
done()