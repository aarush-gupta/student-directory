import turtle
import random
import time
print("avoid the red , green, and yellow . Red move fast, yellow medium, green slow.")
score = 0
lives = 3
turtle.getscreen()
t = turtle.Turtle()
t.shape("circle")
t.pencolor("blue")
r1 = turtle.Turtle()
r2 = turtle.Turtle()
r3 = turtle.Turtle()
r4 = turtle.Turtle()
r5 = turtle.Turtle()
r1.position(random.randint(-300, 300), 300)
r2.position(random.randint(-300, 300), 300)
r3.position(random.randint(-300, 300), 300)
r4.position(random.randint(-300, 300), 300)
r5.position(random.randint(-300, 300), 300)
r1.pencolor("Red")
r2.pencolor("Yellow")
r3.pencolor("Yellow")
r4.pencolor("Green")
r5.pencolor("Green")
while lives != 0:
    score += 1
    r1.position(random.randint(-300, 300), (300-20))
    r2.position(random.randint(-300, 300), (300-10))
    r3.position(random.randint(-300, 300), (300-10))
    r4.position(random.randint(-300, 300), (300-5))
    r5.position(random.randint(-300, 300), (300-5))
    if r5.x == -300:
        r5.position(random.randint(-300, 300), 300)
    if r4.x == -300:
        r4.position(random.randint(-300, 300), 300)
    if r3.x == -300:
        r3.position(random.randint(-300, 300), 300)
    if r2.x == -300:
        r2.position(random.randint(-300, 300), 300)
    if r1.x == -300:
        r1.position(random.randint(-300, 300), 300)
    time.sleep(1)
