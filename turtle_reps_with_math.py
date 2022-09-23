import turtle

length = 120
turn_angle = 45

tom = turtle.Turtle()
tom.speed(0)
tom.goto(3,3)
# time to play with these next 3 lines

for t in range(200):
    #print("length is", length, "angle is", turn_angle)
    tom.forward(length)
    tom.left(turn_angle)
    length = length -3
    #turn_angle = turn_angle



#       + -  / *   **   %         (suggest, if you use exponents, use something like variable**1.05 




#   assign "length" the value of "length + 10"
