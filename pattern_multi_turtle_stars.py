import turtle
import time

# 1. Disable automatic screen updates and enable manual frame-by-frame control
# Without it, turtle updates the screen after every single drawing command, very slow.
# With tracer(0), all drawing happens invisibly in the background.
# turtle.update() then renders everything at once, giving us smooth frame-by-frame animation.
turtle.tracer(0)
turtle.bgcolor("black")  # Premium black background
colors = ["#39FF14", "#FF007F", "#00FFFF", "#7B00FF"]

#colors = ["yellow", "cyan", "lime", "magenta"]
turtles = []

# 2. Initialization: Guide each turtle to its own starting position
for i in range(4):
    t = turtle.Turtle()
    t.shape("circle")   # Use clean circle icons during animation
    t.color(colors[i])
    t.pensize(3)        # Thicker lines to perfectly fill the background gaps
    t.speed(0)
    
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 90) # Face East, North, West, and South
    
    # Spread them out from the center so they create a massive interlocking pattern
    t.forward(150)       
    t.pendown()
    turtles.append(t)

# --- Art Parameters for the Kaleidoscope Pattern ---
drawing_angle = 144  
total_steps = 185    # 🌟 INCREASED STEPS: Allows the stars to grow massive and interlock beautifully

# ━━━ Main Game Loop: Synchronized Frame Animation ━━━
for step in range(total_steps):
    
    # High-density step multiplier (1.75) ensures no black lines inside the stars
    current_distance = 10 + (step * 1.75)
    
    # All 4 turtles move simultaneously in the current frame
    for t in turtles:
        t.forward(current_distance)
        t.right(drawing_angle)
        
    # Render the current frame: display the changes for all turtles at once
    turtle.update()
    
    # Speed Control: Smooth, elegant, and perfectly trackable animation pace
    # search: python pause for seconds
    time.sleep(0.06)

# 3. Clean up the final artwork
for t in turtles:
    t.hideturtle()  # Hide all turtle icons so the final masterpiece is flawless

# Final update to apply the hideturtle changes to the screen
turtle.update()
turtle.done()