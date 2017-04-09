from turtle import *

def rightTurn():
    john.right(90)
    print("John turned right")


def leftTurn():
    john.left(90)
    print("John turned left")


def forward(steps):
    john.forward(10 * steps)
    print("John moved forward")


john = Turtle()

for i in range(0, 100):
    notInput = False
    while not notInput:
        x = input("Enter Direction: ")
        if x.lower() == "left":
            leftTurn()
        elif x.lower() == "right":
            rightTurn()
        elif x.lower() == "forward":
            forward(1)
        elif x.lower().split()[0] == "forward":
            forward(int(x.lower().split()[1]))
        elif x.lower() == "quit":
            quit()
        else:
            notInput = True
