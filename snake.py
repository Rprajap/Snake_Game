# BaSIC import
import turtle
import random
import time

delay = 0.1
sc = 0
hs = 0
# creating bofies
bodies = []
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("green")
s.setup(width=600,height=600)
# Creating a head of screen
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("yellow")
head.fillcolor('red')
#head.goto(-150,0)
head.penup() # to remove line or shadow
head.direction = "stop"

# creating food for snake
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor('yellow')
food.penup()# to remove line or shadow
food.ht()# hide turtle
food.goto(150,200)
food.st()# show turtle
food.direction = "stop"

# creating as scorebord
sb = turtle.Turtle()
#sb.shape("square")
sb.penup()
sb.ht()
sb.goto(-250,250)
sb.write("Score:0  |   Highest score: 0") # to print a  score  first time on screen

# creating function for move in all direction.

def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "rigth":
        head.direction = "left"
        
def moveRight():
    if head.direction != "left":
        head.direction = "right"
        
def moveStop():
    head.direction = "Stop"
    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
        
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)
        
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)
        
# Event Handling

s.listen()
s.onkey(moveUp,"Up")
s.onkey(moveDown,"Down")
s.onkey(moveLeft,'Left')
s.onkey(moveRight,"Right")
s.onkey(moveStop,"space")

# Main program

while True:
    s.update()# to update a screen
    # check collision with border
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)
        
# check collision with food.
    if head.distance(food)<20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        # increase the body of snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)# append the new body in list
        sc = sc+100 # increase the score
        delay = delay-0.001 # Increase the speed
        if sc > hs:
            hs = sc # hupdate a hiest score
        sb.clear()
        sb.write("Score:{} | Highest Score:{}".format(sc,hs))
    
        # move snke body
    for i in range(len(bodies)-1,0,-1): # check len(bodies)-1,0,-1
        x = bodies[i-1].xcor()
        y = bodies[i-1].ycor()
        bodies[i].goto(x,y)
    if len(bodies)>0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x,y)
    move()
        
    # check collision with snake bofy itself
        
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            # hide a body
            for body in bodies:
                body.ht()
            bodies.clear()
            sc = 0
            delay = 0.1
            sb.clear()
            sb.write("Score:{} | Highest score:{}".format(sc,hs))
    time.sleep(delay)
s.mainloop()