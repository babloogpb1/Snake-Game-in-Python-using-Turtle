#Snake Game in python using Turtle.
                                #CED16I011

import turtle
import time 
import random
import threading
from playsound import playsound
import os
import sys

def play(x):                 ### BGM's for actions
    if x=="scroll":
        playsound('menuChange.mp3')
    elif x=="enter":
        playsound('confirm.mp3')
    elif x=="eat":
        playsound('eat.mp3')
    elif x=="over":
        playsound('gameOver.mp3')

hs = open('HiSc.txt','r')     #### reading highscore from a txt file.
sc1 = hs.readlines()
hs.close()

sc = [int(sc1[x]) for x in range(len(sc1))]
hs = max(sc)

screen = 0
delay = 0.1
final = 0
level = 0
flag = 0
score = 0
high_score = int(hs)
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
no1 = 0
pos = [[0, 0], [-10, 70], [-10, 10], [-10, -50], [-10, -110],[-10,-170]]   ### positions of each option in main menu
title = ["New Game", "Multiplayer", "High Scores", "Levels", "Exit"]
pos1 = [[0, 0], [-10, 70], [-10, 10], [-10, -50]]
title2 = ["Easy", "Medium", "Hard"]       ### positions of levels
no = 1
ff = 0 ### food1 state
st = 1
status = 0

# Set up the main window(screen)
wn = turtle.Screen()
wn.title("Snake Game")
wn.setup(width=600, height=600)
wn.bgpic('bgg.png')   ### backgroung image setup
wn.tracer(0)  # Turns off the screen updates

pen = turtle.Turtle()    ### to diplay the intial text
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(-280,-70 )

#playM = threading.Thread(target=mirchi, args=())
#playM.start()
wlcm = "Welcome to my world!!"
for i in range(len(wlcm)):              ### diplaying welcome text
    pen.write("{}".format(wlcm[i]), font=("Courier", 20, "bold"))
    pen.goto(-280+20*(i+1),-70 )
    time.sleep(0.05) 
time.sleep(1)
pen.clear()
screen = 1
wn.bgpic('grass1.png')
wn.update()

pen1 = turtle.Turtle()   ## to display the menu
pen1.speed(0)
pen1.shape("square")
pen1.color("black")
pen1.penup()
pen1.hideturtle()
#pen1.goto(pos[1][0], pos[1][1])

def s():                    #### on downArrow press
    global no, screen
    screen = 1
    if no != 5:
        no = no + 1
        pen1.clear()
        pen1.goto(pos[1][0], pos[1][1])
        playT = threading.Thread(target=play, args=['scroll'])          ### thread to paly music in background
        playT.start()
        for i in range(1,len(pos)):             ### diplaying menu
            pen1.goto(pos[i][0], pos[i][1])
            if i==no:                           ### to highlight the current option
                pen1.write("\n")
                pen1.write(title[i-1],align="center",font=("Arial", 30, "normal", "bold"))
            else:
                pen1.write("\n{}".format(title[i-1]),align="center",font=("Arial", 24, "normal", "bold"))
        return   ### to kill the sound
        playT.join()


def w():                #### on upArrow press
    global no, screen
    screen = 1
    if no != 1:
        no = no - 1
        pen1.clear()
        pen1.goto(pos[1][0], pos[1][1])
        playT = threading.Thread(target=play, args=['scroll'])
        playT.start()
        for i in range(1,len(pos)):
            pen1.goto(pos[i][0], pos[i][1])
            if i==no:
                pen1.write("\n")
                pen1.write(title[i-1],align="center",font=("Arial", 30, "normal", "bold"))
            else:
                pen1.write("\n{}".format(title[i-1]),align="center",font=("Arial", 24, "normal", "bold"))
        return
        playT.join()
        

        
def menu():                ### to display initial menu
    global pen1,pen, screen
    screen = 1
    wn.onkeypress(w, "Up")
    wn.onkeypress(s, "Down")
    pen1.clear()
    for i in range(1,len(pos)):
                pen1.goto(pos[i][0], pos[i][1])
                if i==no:
                    pen1.write("\n")
                    pen1.write(title[i-1],align="center",font=("Arial", 30, "normal", "bold"))
                else:
                    pen1.write("\n{}".format(title[i-1]),align="center",font=("Arial", 24, "normal", "bold"))
    pen1.shapesize(1.5, 1.5, 1) 
    return

menu()


def enter():   ### screens based on option chosen from main menu
    global no, screen, pen1, pen,status,level
    playT = threading.Thread(target=play, args=['enter'])
    playT.start()
    if no==5:
        screen = 5    ### exit screen
    '''if no == 4:
        screen = 6
        pen1.clear()
        pen1.goto(0, 0)
        pen1.write("Easy \n Medium \n Hard",align="center",font=("Arial", 40, "normal", "bold"))    ### levels
        screen = 2
        level = 2
        time.sleep(2)'''
    if screen == 4:             ### highscore screen
        wn.onkeypress(menu, "e")
        wn.onkeypress(w, "Up")
        wn.onkeypress(s, "Down")
        wn.onkeypress(enter, "Return")
        return
    if screen == 6:
        if no1 == 0:
            screen = 2
        if no1 == 1:
            screen = 2
            level = 1
        if no1 == 2:
            screen = 2
            level = 2
         
    if no == 1:
        screen = 2      ### singlePlayer
    if no == 2:
        screen = 3      ### multiPlayer
    if no == 3:
        screen = 4
        pen1.clear()
        pen1.goto(-10, 120)
        pen1.write("High Scores",align="center",font=("Arial", 40, "normal", "bold"))       ### displaying the best 5 highScores read from a file.
        #print(screen,"write")
        for i in range(len(sc)):
            pen1.goto(-10, 50-40*(i+1))
            pen1.write("{}\n".format(sc[i]),align="center",font=("Arial", 20, "normal", "bold"))
        wn.onkeypress(menu, "e")
        return

    if no!=3:    
        pen.clear()
        pen1.clear()
        #print("nothere")
        #cursor.goto(-1000, -1000)
        #cursor.color("light blue")
        pen.goto(0, 260)
    #print(screen,"hehh")
    return
    playT.join()
        

if screen == 1:         ### defining the actions for each keyPress when present on screen 1(main menu)
    wn.update()
    wn.listen()
    wn.onkeypress(w, "Up")
    wn.onkeypress(s, "Down")
    wn.onkeypress(enter, "Return")


zz = 0
while 1:               ### waiting for any option to be choosed. 
    wn.update()
    if screen == 1:
        abc = 1
    else:
        break
        
if screen!=4:
    pen.clear()
    pen1.clear()
while screen==4:
    wn.update()    
    abc = 1
if screen == 1:
    wn.onkeypress(enter, "Return")  
while screen==1:
    wn.update()    
    abc = 1
    
if screen==5:       ### exit function
    sys.exit()

if screen == 2:
    if level == 0:
        '''for i in range(15):         ### generating obstacles randomly on the screen
            blk = turtle.Turtle()
            m = random.randint(-280, 280)
            n = random.randint(-280, 220)   
            blk.goto(m,n)
            blk.speed(0)
            blk.shape("square")
            blk.color("yellow")
            blk.penup()'''
    pen.goto(0, 260)        
    pen.write("Score: 0  High Score: {}".format(int(hs)), align="center", font=("Courier", 20, "normal"))
if screen == 3:
    pen.write("Black: 0  Blue: 0", align="center", font=("Courier", 20, "normal"))

# Snake head
head = turtle.Turtle()              ### head of snake
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(-40, 0)
head.direction = "stop"

# if screen == 3:
head1 = turtle.Turtle()             ### head of 2nd snake in multiPlayer mode
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
food = turtle.Turtle()              ### fruit setup
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
segments = []   ### list to store the body segments
segments1 = []


    # Functions defining the direction of head
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



def move(head2, segment):           ### movement of snakeHead in the specified direction
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


def coll_border(head2, segment):        ### function to check for collison of border and snakeHead
    global score, delay, head, z, final, final1, head1, score1
    if head2.xcor() > 280 or head2.xcor() < -290 or head2.ycor() > 260 or head2.ycor() < -290:
        if head2 == head:
            z = 1
            final = score
            #score = 0
        if head2 == head1:
            z = -1
            final1 = score1
            #score1 = 0

        # Reset the delay
        delay = 0.1


def coll_food(head2, segment):          ### function to check if snake eats a fruit.
    global delay, score, high_score, food, a, b, flag, i, m, n, t, eat, a1, b1, ate, score1, high_score1
    for j in segment:
        if j.distance(a1, b1) < 5:
            j.shapesize(1.5, 1.5, 1)
            # j.color("black")
        else:
            j.shapesize(1, 1, 1)
            # j.color("green")
    if head2.distance(food) < 50 or head2.distance(food1) < 30:  ### opening mouth when near to food
        head2.shapesize(1.5, 1.5, 1)
    else:
        head2.shapesize(1, 1, 1)

        # wn.update()

    if head2.distance(food) < 15:
        playT = threading.Thread(target=play, args=['eat'])
        playT.start()
        head2.shapesize(1, 1, 1)
        a1 = food.xcor()
        b1 = food.ycor()
        a = random.randint(-280, 280)       ### Move the food to a random spot
        b = random.randint(-280, 220)
        # print("bye")

        # Shorten the delay
        delay -= 0.001

        #sem1.acquire()
        if head2 == head:
            ate = 1
        else:
            ate = 2

    if flag != 1:                           ### generating the big fruit randomly
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
    if flag == 1:                           ### check if snake eats big fruit if already present
        if head2.distance(food1) < 25:
            playF = threading.Thread(target=play, args=['eat'])
            playF.start()
            # Move the food to a random spot
            flag = 0
            t = 0
            eat = 1
            # Shorten the delay as the game progresses
            delay -= 0.001

            # Increase the score
            score += 20

            if score > high_score:
                high_score = score
    return


def coll_body(head2, segment):              ### function to check for collison of snakeHead with its own body or the body of other snake in multiPlayer mode
    global z, score, delay, segments, final, final1, head, head1
    if head2 == head:                       ### for singlePlayer
        for i in segments1:
            if i.distance(head2) < 20:
                z = 1
                final = score
                score = 0
                delay = 0.1
    if head2 == head1:                      ### for multiPlayer
        for i in segments:
            if i.distance(head2) < 20:
                z = -1
                final = score
                score = 0

                # Reset the delay
                delay = 0.1
        if head1.distance(head)<20:
                z = -1
                final = score
                score = 0
                delay = 0.1
        for i in segments1:
            if i.distance(head2) < 20:
                z = -1
                final = score
                score = 0
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

            delay = 0.1


def do1(head2, segment):    ### finishing the game when an unwanted collision occurs
    global z,high_score, flag, t, head, head1,segments,segments1, score, score1
    playT = threading.Thread(target=play, args=['over'])
    playT.start()
    pen.clear()
    head.goto(0, 0)
    head.direction = "stop"
    for i in segments1:
        i.goto(1000, 1000)

    segments1.clear()
    head.color("light blue")
    food.clear()
    food1.clear()
    pen.goto(0, 0)
    flag = 0
    t = 0
    # wn.update()
    if screen == 2:     ### for singlePlayer
        head.goto(0, 0)
        head.direction = "stop"
        for i in segment:
            i.goto(1000, 1000)

        segment.clear()
        pen.write("Game Over!! \n Score:{}".format(final), align="center",
              font=("Courier", 20, "normal"))
        print(sc[:])
        if high_score>int(min(sc[:])):          ### updating high score into the file
            sc.append(high_score)
            sc.sort(reverse=True)
            if len(sc)>5:   ### 5 highScores in a file
                sc.pop()
            hs = open('HiSc.txt','w')
            for item in sc:
                hs.write("%d\n" % item)
            hs.close()
        time.sleep(1.5)
        head.color("black")             ### resetting to intial state
        pen.goto(0, 260)
        # score = 0
        pen.clear()
        score = 0
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                  font=("Courier", 20, "normal"))
            
    if screen == 3:         ### for multiPlayer mode
        head1.goto(50, 0)
        head1.direction = "stop"
        # time.sleep(1)
        head1.color('blue')
        for i in segments:
            i.goto(1000, 1000)
        #print("segments",z)
        head1.color("light blue")
        segments.clear()
        if score > score1:          ### determinig the winner based on their scores
            pen.write("Black Wins!! \n Score:{}".format(score), align="center",
                      font=("Courier", 20, "normal"))
        if score < score1:
            pen.write("Blue Wins!! \n Score:{}".format(score1), align="center",
                      font=("Courier", 20, "normal"))
        if score == score1:
            pen.write("Game Draw!! \n Score:{}".format(score), align="center",
                      font=("Courier", 20, "normal"))
                      
        time.sleep(1.5)
        head1.color("blue")         ### resetting to intial state
        pen.clear()
        score = 0
        score1 = 0
        pen.goto(0, 260)
        pen.write("Blue: {}  Black: {}".format(score, score1), align="center",
                  font=("Courier", 20, "normal"))
    playT.join()
    head.color("black")
    food.goto(0, 100)
    food1.goto(1000,1000)
    #head2.color("black")
    food.color("red")
    food1.color("brown")  
    z = 0       ### game isn't over(restarted)



def do2(head2, segment):    ### body incrementing   
    global a, b, a1, b1, ate, score1, score, high_score1, high_score

    # last.goto(a1, b1)
    food.goto(a, b + 1)
    if head2 == head:           ### updating highscore
        score += 10
        if score > high_score:
            high_score = score
    else:
        score1 += 10
        if score1 > high_score1:
            high_score1 = score1
    # Add a segment
    new_segment = turtle.Turtle()           ### creating new segment and adding it to the body(list)
    new_segment.speed(0)
    new_segment.shape("circle")
    if head2 == head:
        new_segment.color("green")
    if head2 == head1:
        new_segment.color("white")

    new_segment.penup()
    segment.append(new_segment)
    pen.clear()
    if screen == 2:             ### displaying the updated score based on the mode
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
              font=("Courier", 20, "normal"))
    if screen == 3:
        pen.write("Blue: {}  Black: {}".format(score1, score), align="center",
                  font=("Courier", 20, "normal"))

    a = 1000
    b = 1000
    ate = -1        ### food is eaten


# Keyboard bindings for snakes direction  
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

if screen == 3:         #### for multiplayer
    wn.onkeypress(go_up1, "w")
    wn.onkeypress(go_down1, "s")
    wn.onkeypress(go_left1, "a")
    wn.onkeypress(go_right1, "d")


def call(head2, segment):   ### movement of snake
    global a, z, flag, m, n, t, eat, i, ff, st
    if z == 1 or z == -1:   ### Finish call if the collison occurs 
        do1(head2, segment)

    if a < 600:
        if head2 == head and ate == 1:
            do2(head2, segment)
        if head2 == head1 and ate == 2:
            do2(head2, segment)
    if flag == 1:           ### timer for bigFruit
        if m < 600:
            food1.goto(m, n)
            m = 1000
            n = 1000
        else:
            t = t + 1

        if t > 40:          ### deleting the bigFruit if timer finishes
            food1.goto(1000, 1000)
            flag = 0
            t = 0
            pen.clear()

            if screen == 2:
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 20, "normal"))
            if screen == 3:
                pen.write("Blue: {}  Black: {}".format(score1, score), align="center",
                          font=("Courier", 20, "normal"))
    if eat == 1:
        pen.clear()
        if screen == 2:
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 20, "normal"))
        if screen == 3:
            pen.write("Blue: {}  Black: {}".format(score1, score), align="center",
                      font=("Courier", 20, "normal"))
        eat = 0
        food1.goto(1000, 1000)

    if t != 0:
        pen.clear()
        if t:
                if ff == 0:    ### for inc/dec size of big fruit(animation) if the bigFruit is present
                    if st == 1:
                        food1.shapesize(1.75, 1.75, 1)
                        st = 2
                    elif st == 2:
                        food1.shapesize(1.5, 1.5, 1)
                        st = 3
                    else:
                        food1.shapesize(1, 1, 1)
                        ff = 1 
                else:
                    if st == 3:
                        food1.shapesize(1.5, 1.5, 1)
                        st = 2
                    elif st == 2:
                        food1.shapesize(1.75, 1.75, 1)
                        st = 1
                    else:
                        food1.shapesize(2, 2, 2)
                        ff = 0 

        if screen == 2:
            pen.write("Score:{} HighScore:{} T-{}".format(score, high_score, 40 - t), align="center",
                      font=("Courier", 20, "normal"))
        if screen == 3:
            pen.write("Blue: {}  Black: {} T-{}".format(score1, score, 40 - t), align="center",
                      font=("Courier", 20, "normal"))

    for index in range(len(segment) - 1, 0, -1):        ### moving each segment the position of its adjacent segment(movement of snake)
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


def player1(head2, segment):            ### threads to check for collision of border, body and food simultaneously
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


if __name__ == "__main__":      ##main loop
    # wn.update()
    if screen == 3:
        while True:
            wn.update()

            g1 = threading.Thread(target=player1, args=(head, segments))        ### running for each snake 
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

