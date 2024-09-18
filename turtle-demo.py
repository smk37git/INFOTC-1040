from turtle import *

# 1. Draw the circle with the radius parameter
# 2. Call itself with a smaller radius
def recursive_circle(t, radius):
    # penup
    t.penup()
    t.forward(10)
    # pendown
    t.pendown()
    
    
    t.circle(radius)
    # base case: when to stop recursive call
    # base case is radius <= 0
    if radius > 0:
        recursive_circle(t, radius-5)
    # No else - do nothing


def main():
    giuseppe = Turtle() # empty parantheses, no arguements
    giuseppe.shape("turtle")
    # Move the turtle forward for some steps
    giuseppe.speed(4)
    recursive_circle(giuseppe, 50)
    done()
    
main()