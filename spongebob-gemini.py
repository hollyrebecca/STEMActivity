import turtle

# Setup the drawing window
screen = turtle.Screen()
screen.title("SpongeBob SquarePants in Python Turtle")
screen.setup(width=600, height=700)
screen.bgcolor("#4682B4") # Ocean blue background

t = turtle.Turtle()
t.speed(0) # Fastest drawing speed

# --- Helper Functions ---

def draw_rect(t, x, y, w, h, fill, border="black", pensize=3):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pensize(pensize)
    t.pencolor(border)
    t.fillcolor(fill)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()

def draw_circle(t, x, y, r, fill, border="black", pensize=3):
    t.penup()
    t.goto(x, y - r) # Center the circle at (x, y)
    t.setheading(0)
    t.pensize(pensize)
    t.pencolor(border)
    t.fillcolor(fill)
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# --- Drawing SpongeBob ---

# 1. Main Body Parts
# Yellow Sponge Body
draw_rect(t, -100, 150, 200, 180, "#FFF200") 
# White Shirt
draw_rect(t, -100, -30, 200, 25, "white")
# Brown Pants
draw_rect(t, -100, -55, 200, 45, "#603913")

# 2. Spongy Pores (Green Spots)
draw_circle(t, -75, 110, 10, "#CCD122", border="#CCD122")
draw_circle(t, 75, 90, 12, "#CCD122", border="#CCD122")
draw_circle(t, -70, -10, 8, "#CCD122", border="#CCD122")
draw_circle(t, 65, -15, 10, "#CCD122", border="#CCD122")

# 3. Legs and Shoes
# Pant Sleeves
draw_rect(t, -60, -100, 30, 12, "#603913")
draw_rect(t, 30, -100, 30, 12, "#603913")
# Yellow Legs
draw_rect(t, -51, -112, 12, 35, "#FFF200")
draw_rect(t, 39, -112, 12, 35, "#FFF200")
# Socks (White)
draw_rect(t, -51, -147, 12, 20, "white")
draw_rect(t, 39, -147, 12, 20, "white")
# Black Shoes
draw_circle(t, -55, -172, 12, "black")
draw_rect(t, -70, -167, 25, 12, "black")
draw_circle(t, 35, -172, 12, "black")
draw_rect(t, 20, -167, 25, 12, "black")

# 4. Arms and Hands
# Sleeves
draw_rect(t, -115, -20, 15, 15, "white")
draw_rect(t, 100, -20, 15, 15, "white")
# Yellow Arms
draw_rect(t, -111, -35, 7, 40, "#FFF200")
draw_rect(t, 104, -35, 7, 40, "#FFF200")
# Hands
draw_circle(t, -108, -80, 8, "#FFF200")
draw_circle(t, 108, -80, 8, "#FFF200")

# 5. Suit Details (Tie & Collars)
# White Collars
t.penup()
t.goto(-25, -30)
t.begin_fill()
t.fillcolor("white")
t.pendown()
t.goto(-5, -30)
t.goto(-15, -42)
t.goto(-25, -30)
t.end_fill()

t.penup()
t.goto(5, -30)
t.begin_fill()
t.fillcolor("white")
t.pendown()
t.goto(25, -30)
t.goto(15, -42)
t.goto(5, -30)
t.end_fill()

# Red Tie
t.penup()
t.goto(-8, -35)
t.begin_fill()
t.fillcolor("#E41B1B")
t.pendown()
t.goto(8, -35)
t.goto(12, -65)
t.goto(0, -80)
t.goto(-12, -65)
t.goto(-8, -35)
t.end_fill()

# Pants Belt Loops
draw_rect(t, -75, -62, 18, 7, "black")
draw_rect(t, -30, -62, 18, 7, "black")
draw_rect(t, 12, -62, 18, 7, "black")
draw_rect(t, 57, -62, 18, 7, "black")

# 6. Face (Eyes & Eyelashes)
# Big White Eyes
draw_circle(t, -28, 65, 28, "white")
draw_circle(t, 28, 65, 28, "white")
# Blue Irises
draw_circle(t, -20, 65, 12, "#00AEEF")
draw_circle(t, 20, 65, 12, "#00AEEF")
# Black Pupils
draw_circle(t, -20, 65, 6, "black")
draw_circle(t, 20, 65, 6, "black")

# Eyelashes
eyelashes = [
    ((-43, 90), (-53, 104)), ((-28, 93), (-28, 109)), ((-13, 90), (-3, 104)), # Left
    ((13, 90), (3, 104)), ((28, 93), (28, 109)), ((43, 90), (53, 104))       # Right
]
t.pensize(3)
for start, end in eyelashes:
    t.penup()
    t.goto(start)
    t.pendown()
    t.goto(end)

# 7. Mouth & Iconic Teeth
# Open Smile
t.penup()
t.goto(-50, 15)
t.setheading(-60)
t.pendown()
t.begin_fill()
t.fillcolor("#7A1F1D") # Inside mouth color
t.circle(50, 120)
t.goto(-50, 15)
t.end_fill()

# Two Buck Teeth
draw_rect(t, -16, 15, 12, 14, "white")
draw_rect(t, 4, 15, 12, 14, "white")

# 8. Cheeks & Nose (Overlapping details)
# Rosy Cheeks
draw_circle(t, -55, 22, 10, "#FF7F27", border="#FF7F27")
draw_circle(t, 55, 22, 10, "#FF7F27", border="#FF7F27")

# Freckles
t.penup()
freckles_loc = [(-58, 24), (-54, 18), (-50, 25), (50, 25), (54, 18), (58, 24)]
for loc in freckles_loc:
    t.goto(loc)
    t.dot(3, "#D11A2A")

# The Nose
draw_circle(t, 0, 45, 11, "#FFF200")

# Hide turtle and keep window open
t.hideturtle()
screen.mainloop()