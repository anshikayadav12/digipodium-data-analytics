from turtle import *
speed('fastest')
bgcolor('black')
colors = ['red','orange','yellow','green','blue']

i = 0
while True:
    pencolor(colors[i%5])
    fd(10+i)
    lt(200)

    i += 1
mainloop()