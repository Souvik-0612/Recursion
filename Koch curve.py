# -::- Fractal -::-
from turtle import *
def koch(L, n):
	if n == 0:
		fd(L)
	else:
		koch(L/3, n-1)
		lt(60)
		koch(L/3, n-1)
		rt(120)
		koch(L/3, n-1)
		lt(60)
		koch(L/3, n-1)
		
		

	
speed(0)	
		
penup()
goto(-500, 0)
pendown()
width(4)
koch(1000, 4)
hideturtle()
done()