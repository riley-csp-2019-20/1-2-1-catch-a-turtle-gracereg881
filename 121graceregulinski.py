# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration---- # define shape, size, color
shape = "turtle"
size = 5
color = "violet"
score = 0

#-----initialize turtle----- # events
jack = trtl.Turtle(shape = shape)
jack.color(color)
jack.shapesize(size)
jack.speed(0)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-370,270)
font = ("Arial" , 80 , "bold")
score_writer.write("=)", font = font)


#-----game functions-------- #
def turtle_clicked(x,y):
    print("jack was clicked!")
    change_position()
    score_counter()

def change_position():
    jack.penup()
    jack.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    jack.goto(new_xpos, new_ypos)
    jack.st()

def score_counter():
    global score
    score+=1
    print(score)


#-----events----------------
jack.onclick(turtle_clicked)

wn=trtl.Screen()
wn.mainloop()