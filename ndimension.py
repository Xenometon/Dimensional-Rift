#This code will result in a mystic dimensional figure 👀

#Importing module

import turtle as t

t.speed(0)
t.bgcolor('white')
t.pencolor('black')

for i in range(275):
    t.right(i)
    t.circle(250,i)
    t.forward(i)
    t.right(90)
t.done()

#End of the program