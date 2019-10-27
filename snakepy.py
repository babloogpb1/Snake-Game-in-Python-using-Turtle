import turtle
import time #
import random
import threading

screen = 0
# import tkinter
delay = 0.1
final = 0
# Score
flag = 0
score = 0
high_score = 0
#sem1 = threading.Semaphore()
#fruitlock = threading.Semaphore()
final1 = 0
flag1 = 0
score1 = 0
high_score1 = 0
a = 1000
b = 1000
n = 1000
m = 1000
z = 0
i = 0
t = 0
ate = -1
eat = 0
pos = [[0, 0], [-105, 50], [-105, 15], [-120, -25], [-60, -60]]   ### cursor(Tri) position array
no = 1
# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("light blue")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

cursor = turtle.Turtle()
cursor.speed(0)
cursor.shape("triangle")
# food.shapesize(2, 2, 1)
cursor.color("red")
cursor.penup()
cursor.goto(-105, 50)

# while 1:
#   cd = 1

# Pen
# sc = turtle.Screen()

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
# sc.bgpic("g2.jpg")
# sc.setup(width=600, height=600, startx=0, starty=0)

# sc.update()

pen.write("welcome to my world!! \n                -python", align="center", font=("Courier", 24, "normal"))
time.sleep(1.5)
pen.clear()
screen = 1

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.shape("square")
pen1.color("black")
pen1.penup()
pen1.hideturtle()
pen1.goto(0, -80)
pen1.write("\n\n\n\n New Game\n Multiplayer\nHigh  Scores\n      Exit", align="center",
           font=("Arial", 24, "normal", "bold"))
pen1.shapesize(1.5, 1.5, 1)


def s():
    global no
    if no != 4:
        no = no + 1
        cursor.goto(pos[no][0], pos[no][1])


def w():
    global no
    if no != 1:
        no = no - 1
        cursor.goto(pos[no][0], pos[no][1])


def enter():
    global no, screen
    if no == 1:
        screen = 2
    if no == 2:
        screen = 3


wn.update()
wn.listen()

if screen == 1:
    wn.onkeypress(w, "Up")
    wn.onkeypress(s, "Down")
    wn.onkeypress(enter, "Return")

zz = 0
while 1:
    wn.update()
    if screen == 1:
        abc = 1
    else:
        break
    # zz = zz + 1
pen.clear()
pen1.clear()
cursor.goto(-1000, -1000)
cursor.color("light blue")
pen.goto(0, 260)
if screen == 2:
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
if screen == 3:
    pen.write("Black: 0  Blue: 0", align="center", font=("Courier", 24, "normal"))

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(-40, 0)
head.direction = "stop"

# if screen == 3:
head1 = turtle.Turtle()
head1.speed(0)
head1.shape("circle")
head1.color("blue")
head1.penup()
head1.goto(40, 0)
head1.direction = "stop"

if screen == 2:
    head1.goto(1000, 1000)
    head1.color("light blue")
# wn.update()

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
# food.shapesize(2, 2, 1)
food.color("red")
food.penup()
food.goto(0, 100)
a1 = food.xcor()
b1 = food.ycor()

food1 = turtle.Turtle()
food1.speed(0)
food1.shape("circle")
food1.shapesize(2, 2, 1)
food1.color("brown")
food1.penup()
food1.goto(1000, 1000)
segments = []
segments1 = []


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_up1():
    if head1.direction != "down":
        head1.direction = "up"


def go_down1():
    if head1.direction != "up":
        head1.direction = "down"


def go_left1():
    if head1.direction != "right":
        head1.direction = "left"


def go_right1():
    if head1.direction != "left":
        head1.direction = "right"


def move(head2, segment):
    # print("he;llo")
    if head2.direction == "up":
        y = head2.ycor()
        head2.sety(y + 20)

    if head2.direction == "down":
        y = head2.ycor()
        head2.sety(y - 20)

    if head2.direction == "left":
        x = head2.xcor()
        head2.setx(x - 20)

    if head2.direction == "right":
        x = head2.xcor()
        head2.setx(x + 20)


def coll_border(head2, segment):
    global score, delay, head, z, final, final1, head1, score1
    if head2.xcor() > 280 or head2.xcor() < -290 or head2.ycor() > 260 or head2.ycor() < -290:
        if head2 == head:
            z = 1
            final = score
            score = 0
        if head2 == head1:
            z = -1
            final1 = score1
            score1 = 0

        # Reset the delay
        delay = 0.1


def coll_food(head2, segment):
    global delay, score, high_score, food, a, b, flag, i, m, n, t, eat, a1, b1, ate, score1, high_score1
    # pen.write(": {} ".format(head.distance(food)), align="center", font=("Courier", 24, "normal"))
    # print("hii")
    for j in segment:
        if j.distance(a1, b1) < 5:
            j.shapesize(1.5, 1.5, 1)
            # j.color("black")
        else:
            j.shapesize(1, 1, 1)
            # j.color("green")
    if head2.distance(food) < 50 or head2.distance(food1) < 30:
        head2.shapesize(1.5, 1.5, 1)
    else:
        head2.shapesize(1, 1, 1)

        # wn.update()

    if head2.distance(food) < 15:
        # Move the food to a random spot

        head2.shapesize(1, 1, 1)
        a1 = food.xcor()
        b1 = food.ycor()
        a = random.randint(-280, 280)
        b = random.randint(-280, 220)
        # print("bye")

        # Shorten the delay
        delay -= 0.001

        # Increase the score
    #friuts = (int)malloc((sizeof(int)))


        #sem1.acquire()
        if head2 == head:
            ate = 1
        else:
            ate = 2

    if flag != 1:
        ran = random.randint(1, 10)

        if i % ran == 0 and i % 70 == 0 and i != 0 and head2.xcor() != 0:
            while True:
                m = random.randint(-280, 280)
                n = random.randint(-280, 220)
                if m != food.xcor() and n != food.ycor():
                    t = 1
                    flag = 1
                    break
    #sem1.release()
    if flag == 1:
        if head2.distance(food1) < 25:
            # Move the food to a random spot
            flag = 0
            t = 0
            eat = 1
            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 20

            if score > high_score:
                high_score = score


def coll_body(head2, segment):
    global z, score, delay, segments, final, final1
    if head2 == head:
        for i in segments1:
            if i.distance(head2) < 20:
                z = 1
                final = score
                score = 0

                # Reset the delay
                delay = 0.1
    if head2 == head1:
        for i in segments:
            if i.distance(head2) < 20:
                z = -1
                final = score
                score = 0

                # Reset the delay
                delay = 0.1
    for i in segment:
        if i.distance(head2) < 20:
            if head2 == head:
                z = 1
                final = score

            else:
                z = -1
            # Reset the score
            final = score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display


def do1(head2, segment):
    global z,high_score

    head2.goto(0, 0)
    head2.direction = "stop"
    # time.sleep(1)

    for i in segment:
        i.goto(1000, 1000)

    segment.clear()

    pen.clear()
    head2.color("light blue")
    food.color("light blue")
    food1.color("light blue")

    pen.goto(0, 0)

    # wn.update()
    if screen == 2:
       # f = open("score.txt","r+")
        #h = f.read()
        #if ord(h) < high_score:
         #   f.write(ord(high_score))
        pen.write("Game Over!! \n Score:{}".format(final), align="center",
              font=("Courier", 24, "normal"))
    if screen == 3:
        if score > score1:
            pen.write("Black Wins!! \n Score:{}".format(score), align="center",
                      font=("Courier", 24, "normal"))
        if score < score1:
            pen.write("Blue Wins!! \n Score:{}".format(score1), align="center",
                      font=("Courier", 24, "normal"))
        if score == score1:
            pen.write("Game Draw!! \n Score:{}".format(score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(1.5)
    food.goto(0, 100)

    head2.color("black")
    food.color("red")
    food1.color("brown")

    pen.goto(0, 260)
    # score = 0
    pen.clear()

    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
              font=("Courier", 24, "normal"))

    z = 0



def do2(head2, segment):
    global a, b, a1, b1, ate, score1, score, high_score1, high_score

    # last.goto(a1, b1)
    food.goto(a, b + 1)
    if head2 == head:
        score += 10
        if score > high_score:
            high_score = score
    else:
        score1 += 10
        if score1 > high_score1:
            high_score1 = score1
    # Add a segment
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("circle")
    if head2 == head:
        new_segment.color("green")
    if head2 == head1:
        new_segment.color("white")

    new_segment.penup()
    segment.append(new_segment)
    pen.clear()
    if screen == 2:
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
              font=("Courier", 24, "normal"))
    if screen == 3:
        pen.write("Blue: {}  Black: {}".format(score1, score), align="center",
                  font=("Courier", 24, "normal"))

    a = 1000
    b = 1000
    ate = -1


# Keyboard bindings

# if screen == 2:
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

if screen == 3:
    wn.onkeypress(go_up1, "w")
    wn.onkeypress(go_down1, "s")
    wn.onkeypress(go_left1, "a")
    wn.onkeypress(go_right1, "d")


def call(head2, segment):
    global a, z, flag, m, n, t, eat, i
    if z == 1 or z == -1:
        do1(head2, segment)

    if a < 600:
        if head2 == head and ate == 1:
            do2(head2, segment)
        if head2 == head1 and ate == 2:
            do2(head2, segment)
    if flag == 1:
        if m < 600:
            food1.goto(m, n)
            m = 1000
            n = 1000
        else:
            t = t + 1

        if t > 40:
            food1.goto(1000, 1000)
            flag = 0
            t = 0
            pen.clear()

            if screen == 2:
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))
            if screen == 3:
                pen.write("Blue: {}  Black: {}".format(score1, score), align="center",
                          font=("Courier", 24, "normal"))
    if eat == 1:
        pen.clear()
        if screen == 2:
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))
        if screen == 3:
            pen.write("Blue: {}  Black: {}".format(score1, score), align="center",
                      font=("Courier", 24, "normal"))
        eat = 0
        food1.goto(1000, 1000)

    if t != 0:
        pen.clear()


        if screen == 2:
            pen.write("Score:{} HighScore:{} time:{}".format(score, high_score, 40 - t), align="center",
                      font=("Courier", 24, "normal"))
        if screen == 3:
            pen.write("Blue: {}  Black: {} time{}".format(score1, score, 40 - t), align="center",
                      font=("Courier", 24, "normal"))

    for index in range(len(segment) - 1, 0, -1):
        x = segment[index - 1].xcor()
        y = segment[index - 1].ycor()

        segment[index].goto(x, y)
        # wn.update()

        # Move segment 0 to where the head is
    if len(segment) > 0:
        x = head2.xcor()
        y = head2.ycor()
        segment[0].goto(x, y)
        if segment[0].distance(a1, b1) < 5:
            segment[0].shapesize(1.5, 1.5, 1)
        else:
            segment[0].shapesize(1, 1, 1)

    move(head2, segment)
    i = i + 1
    # time.sleep(delay)
    wn.update()


def player1(head2, segment):
    global flag, eat, t, i, m, n
    t1 = threading.Thread(target=coll_border, args=(head2, segment))
    t2 = threading.Thread(target=coll_food, args=(head2, segment))
    t3 = threading.Thread(target=coll_body, args=(head2, segment))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    # time.sleep(1)


if __name__ == "__main__":
    # wn.update()
    if screen == 3:
        while True:
            wn.update()

            g1 = threading.Thread(target=player1, args=(head, segments))
            g2 = threading.Thread(target=player1, args=(head1, segments1))
            g1.start()
            g2.start()
            # t3.start()
            g1.join()
            g2.join()

            call(head, segments)
            call(head1, segments1)
            time.sleep(delay)
    if screen == 2:
        while True:
            wn.update()

            g1 = threading.Thread(target=player1, args=(head, segments))
            # g2 = threading.Thread(target=player1, args=(head1, segments1))
            g1.start()
            # g2.start()
            # t3.start()
            g1.join()
            # g2.join()

            call(head, segments)
            # call(head1, segments1)
            time.sleep(delay)

wn.mainloop()
