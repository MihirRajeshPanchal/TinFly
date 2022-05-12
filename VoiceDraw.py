from STT import *
from TTS import *
import turtle
from turtle import *

def voicedraw():
    tts("Speak a thing to draw")
    drawquery=rstt()
    print("drawquery : ",drawquery)
    if drawquery.count('circle')>0:
        drawcircle()
    elif drawquery.count('rectangle')>0:
        drawrectangle()
    elif drawquery.count('triangle')>0:
        drawtriangle()
    elif drawquery.count('star')>0:
        drawstar()
    elif drawquery.count('square')>0:
        drawsquare()
    else:
        drawtext(drawquery)
    

def drawcircle():
    turtle.circle(80)
    turtle.exitonclick()

def drawsquare():
    t = turtle.Turtle()
    # drawing first side
    t.up()
    t.goto(-150,-100)
    t.down()
    t.forward(400) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
    
    # drawing second side
    t.forward(400) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
    
    # drawing third side
    t.forward(400) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
    
    # drawing fourth side
    t.forward(400) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
    turtle.exitonclick()
    
def drawrectangle():
    t = turtle.Turtle()
    t.up()
    t.goto(-150,-100)
    t.down()
    for _ in range(4):
   
  # drawing length
        if _% 2 == 0:
            t.forward(400) # Forward turtle by l units
            t.left(90) # Turn turtle by 90 degree
        
        # drawing width
        else:
            t.forward(200) # Forward turtle by w units
            t.left(90)
            
    turtle.exitonclick()
def drawtriangle():
    t = turtle.Turtle()
    t.forward(100) # draw base
    t.left(120)
    t.forward(100)
    
    t.left(120)
    t.forward(100)
    turtle.exitonclick()

def drawstar():
    t = turtle.Turtle()
 
# executing loop 5 times for a star
    for i in range(5):
    
            # moving turtle 100 units forward
            t.forward(100)
    
            # rotating turtle 144 degree right
            t.right(144)
    turtle.exitonclick()
    

def drawtext(drawquery):
    turtle.write(drawquery, font=("Arial", 16, "normal"))
    turtle.exitonclick()
    
voicedraw()