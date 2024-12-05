import turtle
import time


delay = 0.1

#setting up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height= 600)
wn.tracer(0) #turns off the screen updates

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "up"
head.direction = "left"
head.direction = "right"
head.direction = "down"

#functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.sety(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.sety(x + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)


#Main game loop
while True:
    wn.update()
    
    move()

    time.sleep(delay)


wn.mainloop()