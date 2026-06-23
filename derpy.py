import turtle

def setup_screen():
    screen = turtle.Screen()
    screen.setup(650, 650)
    #screen.title("Derpy Tiger Premium - K-Pop Demon Hunters")
    screen.bgcolor("#EBF5FB") # Crisp pastel background
    return screen

# Helper function for outlined shapes
def draw_shape(t, fill, border="#1A252C", width=4):
    t.pensize(width)
    t.pencolor(border)
    t.fillcolor(fill)
    t.begin_fill()

def draw_circle(t, x, y, radius, fill, border="#1A252C", width=4):
    t.penup()
    t.goto(x, y - radius)
    t.setheading(0)
    t.pendown()
    draw_shape(t, fill, border, width)
    t.circle(radius)
    t.end_fill()

def draw_stripe(t, points, fill="#1B4F72"):
    t.penup()
    t.goto(points[0])
    t.pendown()
    draw_shape(t, fill, border=fill, width=1)
    for pt in points[1:]:
        t.goto(pt)
    t.goto(points[0])
    t.end_fill()

def draw_paw(t, x, y, size):
    # Main paw pad
    draw_circle(t, x, y, size, "#3498DB")
    # Toes
    draw_circle(t, x - size*0.6, y + size*0.8, size*0.35, "#3498DB")
    draw_circle(t, x, y + size*1.1, size*0.35, "#3498DB")
    draw_circle(t, x + size*0.6, y + size*0.8, size*0.35, "#3498DB")

def main():
    screen = setup_screen()
    #turtle.tracer(0, 0) # Instant rendering
    
    t = turtle.Turtle()
    t.speed(0)#t.hideturtle()
    
    # Palette
    FUR_BLUE = "#3498DB"
    DARK_BLUE = "#2471A3"
    STRIPE_COLOR = "#1B4F72"
    MUZZLE_WHITE = "#FFFFFF"
    TONGUE_PINK = "#FF7675"
    OUTLINE = "#1A252C"
    BLUSH = "#FADBD8"
    
    # ---- 1. Ears ----
    # Left Ear
    draw_circle(t, -95, 95, 42, FUR_BLUE)
    draw_circle(t, -93, 93, 24, TONGUE_PINK)
    # Right Ear
    draw_circle(t, 95, 95, 42, FUR_BLUE)
    draw_circle(t, 93, 93, 24, TONGUE_PINK)
    
    # ---- 2. Main Head Base ----
    draw_circle(t, 0, -10, 130, FUR_BLUE)
    
    # ---- 3. Premium Tiger Stripes ----
    # Center forehead
    draw_stripe(t, [(-15, 115), (15, 115), (8, 90), (0, 65), (-8, 90)])
    # Left forehead
    draw_stripe(t, [(-55, 100), (-35, 108), (-30, 85), (-45, 70)])
    # Right forehead
    draw_stripe(t, [(55, 100), (35, 108), (30, 85), (45, 70)])
    # Side Cheek Stripes (Left)
    draw_stripe(t, [(-128, -5), (-120, 10), (-95, 0)])
    draw_stripe(t, [(-125, -30), (-118, -15), (-95, -20)])
    # Side Cheek Stripes (Right)
    draw_stripe(t, [(128, -5), (120, 10), (95, 0)])
    draw_stripe(t, [(125, -30), (118, -15), (95, -20)])
    
    # ---- 4. Cute Blushing Cheeks ----
    draw_circle(t, -90, -25, 18, BLUSH, border=BLUSH)
    draw_circle(t, 90, -25, 18, BLUSH, border=BLUSH)
    
    # ---- 5. Muzzle & Face Base ----
    draw_circle(t, 0, -60, 48, MUZZLE_WHITE)
    
    # ---- 6. Goofy Asymmetrical Eyes ----
    # Left Eye (Big and round)
    draw_circle(t, -48, 25, 32, "white")
    # Right Eye (Smaller and slightly lower for that classic derp look)
    draw_circle(t, 48, 15, 24, "white")
    
    # Pupils pointing completely away from each other
    draw_circle(t, -62, 35, 12, OUTLINE) # Left pupil looking up/out
    draw_circle(t, 54, 8, 9, OUTLINE)    # Right pupil looking down/out
    
    # Eye Highlights
    draw_circle(t, -65, 40, 4, "white", border="white")
    draw_circle(t, 52, 10, 3, "white", border="white")
    
    # ---- 7. Nose & Mouth ----
    # Soft triangle nose
    t.penup()
    t.goto(-14, -22)
    t.pendown()
    draw_shape(t, OUTLINE, OUTLINE, 1)
    t.goto(14, -22)
    t.goto(0, -36)
    t.goto(-14, -22)
    t.end_fill()
    
    # Big happy open mouth
    t.penup()
    t.goto(-35, -45)
    t.pendown()
    draw_shape(t, OUTLINE, OUTLINE, 2)
    t.setheading(-75)
    t.circle(36, 150)
    t.goto(-35, -45)
    t.end_fill()
    
    # Derpy side-flopping tongue
    t.penup()
    t.goto(-15, -55)
    t.pendown()
    draw_shape(t, TONGUE_PINK, OUTLINE, 3)
    t.setheading(-110)
    t.circle(18, 160)
    t.goto(10, -52)
    t.end_fill()
    
    # ---- 8. Little Paws ----
    draw_paw(t, -75, -135, 24)
    draw_paw(t, 75, -135, 24)
    
   
    turtle.update()
    screen.mainloop()

if __name__ == "__main__":
    main()