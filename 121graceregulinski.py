# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration---- # define shape, size, color
shape = "turtle"
size = 5
color = "violet"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle----- # events
jack = trtl.Turtle(shape = shape)
jack.color(color)
jack.shapesize(size)
jack.speed(0)
counter =  trtl.Turtle()

score_writer = trtl.Turtle()
score_writer.pencolor("indigo")
score_writer.penup()
score_writer.goto(-370,270)
font = ("Arial" , 50 , "bold")
score_writer.write(score, font = font)


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
    score_writer.clear()
    score_writer.write(score, font=font)

def countdown():
    global timer, timer_up
    counter.up()
    counter.goto(250, 320)
    counter.down()
    counter.clear()
    if timer <= 0:
        counter.up()
        counter.goto(0,0)
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        game_over()
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

def game_over():
    wn.bgcolor("yellow")
    jack.ht()
    jack.goto(500,500)
    counter.goto(0,0)

    


#-----events----------------
jack.onclick(turtle_clicked)

wn=trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()