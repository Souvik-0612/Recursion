from turtle import*
def square(a):
	for i in range(4):
		fd(a)
		lt(90)
def sq_arc(b):
	square(b)
	circle(b,90)
def fib(c):
	if c == 0:
		return 1
	elif c == 1:
		return 1
	else:
		return fib(c-1)+fib(c-2)

L = []

for i in range(20):
	L.append(fib(i))
	
l = []

for i in range(20):
	l.append(L[i])
	

for i in l:
	sq_arc(i)	

done()