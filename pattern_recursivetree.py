import turtle

# Create a screen and a turtle instance
screen = turtle.Screen()
t = turtle.Turtle()

# Set turtle speed and color
t.speed('fastest')
t.color('blue')

# Rotate the turtle to point upward
t.left(90)

# The recursive fractal function
def draw_fractal(length, depth):
    if depth == 0:
        return  # Base case to stop recursion
    
    # Draw main branch
    t.forward(length)
    
    # Save current position and heading
    pos = t.pos()
    heading = t.heading()

    # Draw left branch (recursive call)
    t.left(35)
    draw_fractal(length * 0.7, depth - 1)

    # Restore position and heading
    t.setheading(heading)
    t.setposition(pos)
    
    # Draw right branch (recursive call)
    t.right(35)
    draw_fractal(length * 0.7, depth - 1)
    
    # Restore position and heading before exiting function
    t.setheading(heading)
    t.setposition(pos)

# To generate a symmetric, circular design like the one in your image, 
# you need to call the fractal function multiple times at different angles.
def draw_symmetrical_pattern(number_of_fractals, length, depth):
    angle = 360 / number_of_fractals
    for i in range(number_of_fractals):
        draw_fractal(length, depth)
        t.right(angle)
        # Re-set heading after each fractal to maintain vertical starting point
        t.setheading(90)

# Set the background to black to match the visual
screen.bgcolor('white')

# Draw the pattern with six main fractal structures
draw_symmetrical_pattern(6, 100, 7)

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()