import turtle

# 1. Set up the display window
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Vortex Spiral")

# 2. Set up the turtle
t = turtle.Turtle()
t.speed(0)  # 0 is the fastest speed possible

# 3. Define a list of vibrant colors
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# 4. Draw the pattern
for x in range(360):
    t.pencolor(colors[x % 6])     # Cycle through the 6 colors
    t.width(x // 100 + 1)         # Gradually make the line thicker
    t.forward(x)                  # Move forward by an increasing distance
    t.left(59)                    # Turn left by 59 degrees (creates the twist)

# 5. Keep the window open when finished
turtle.done()