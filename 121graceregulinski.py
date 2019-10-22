# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

#-----game configuration---- # define shape, size, color
shape = "turtle"
size = 8
color = "violet"

#-----initialize turtle----- # events
jack = trtl.Turtle(shape = shape)
jack.color(color)
jack.shapesize(size)

#-----game functions-------- #


#-----events----------------

wn=trtl.Screen()
wn.mainloop()