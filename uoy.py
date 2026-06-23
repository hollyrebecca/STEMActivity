import turtle

def setup_screen():
    screen = turtle.Screen()
    screen.setup(700, 700)
    screen.title("University of York - Central Hall & Campus Lake")
    screen.bgcolor("#F4F6F7")
    return screen

def draw_filled_rect(t, x, y, width, height, color, border_color=None):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    if border_color:
        t.pencolor(border_color)
    else:
        t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def draw_polygon(t, points, fill_color, border_color=None, line_width=1):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.pensize(line_width)
    if border_color:
        t.pencolor(border_color)
    else:
        t.pencolor(fill_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    for pt in points[1:]:
        t.goto(pt)
    t.goto(points[0])
    t.end_fill()

def draw_goose(t, x, y):
    """Draws a cute, stylized campus goose (a nod to York's famous waterfowl)"""
    # Body
    draw_polygon(t, [(x, y), (x+40, y), (x+50, y+20), (x+25, y+30), (x, y+15)], "white", "#95A5A6", 1)
    # Wing
    draw_polygon(t, [(x+15, y+8), (x+35, y+8), (x+25, y+20)], "#BDC3C7", "#95A5A6", 1)
    # Neck & Head
    draw_polygon(t, [(x+5, y+12), (x-8, y+35), (x-2, y+42), (x+12, y+15)], "white", "#95A5A6", 1)
    # Beak
    draw_polygon(t, [(x-2, y+42), (x-12, y+39), (x-5, y+36)], "#E67E22")
    # Feet
    t.penup()
    t.pensize(2)
    t.pencolor("#E67E22")
    t.goto(x+15, y)
    t.pendown()
    t.goto(x+12, y-8)
    t.goto(x+8, y-8)
    t.penup()
    t.goto(x+28, y)
    t.pendown()
    t.goto(x+25, y-8)
    t.goto(x+21, y-8)

def main():
    screen = setup_screen()
    #turtle.tracer(0, 0)  # Render instantly
    
    t = turtle.Turtle()
    t.speed(0)#t.hideturtle()
    
    # Color Palette (York Branding & Architecture)
    YORK_CREST_BLUE = "#0F2C59"
    SKY_BLUE = "#EBF5FB"
    LAKE_BLUE = "#2E86C1"
    LAKE_SHADOW = "#21618C"
    CONCRETE_LIGHT = "#EAEDED"
    CONCRETE_MED = "#D5DBDB"
    CONCRETE_DARK = "#95A5A6"
    GLASS_BLUE = "#AED6F1"
    GRASS_GREEN = "#27AE60"
    
    # ---- 1. Background Sky & Scenery ----
    draw_filled_rect(t, -360, 360, 720, 420, SKY_BLUE) # Sky
    draw_filled_rect(t, -360, -60, 720, 300, LAKE_BLUE) # Lake Derwent
    
    # Distant backdrop trees/hills
    draw_polygon(t, [(-360, -60), (-250, -40), (-120, -60)], "#1E8449")
    draw_polygon(t, [(120, -60), (220, -45), (360, -60)], "#1E8449")
    
    # ---- 2. Central Hall Support Structure (Pillars & Base) ----
    # Concrete structural columns reaching into the lake
    pillar_x_coords = [-130, -90, -50, -10, 30, 70, 110]
    for px in pillar_x_coords:
        draw_filled_rect(t, px, -35, 12, 55, CONCRETE_DARK)
    
    # Main lower concrete deck platform
    draw_polygon(t, [(-160, -35), (160, -35), (145, -55), (-145, -55)], CONCRETE_MED)
    
    # ---- 3. Central Hall Main Tiers (Brutalist Spaceship Design) ----
    # Tier 1: Lower Slanted Concrete Ring
    draw_polygon(t, [(-165, -35), (165, -35), (180, 5), (-180, 5)], CONCRETE_LIGHT, CONCRETE_MED, 1)
    
    # Tier 2: Mid-level Glass & Panels Window Band
    draw_polygon(t, [(-175, 5), (175, 5), (155, 35), (-155, 35)], GLASS_BLUE, CONCRETE_DARK, 1)
    # Add structural window mullions vertical details
    for wx in range(-150, 160, 25):
        t.penup()
        t.goto(wx * 1.1, 5)
        t.pendown()
        t.pencolor(CONCRETE_DARK)
        t.goto(wx * 0.95, 35)
        
    # Tier 3: Massive Concrete Upper Crown (The Hanging Saucer)
    draw_polygon(t, [(-190, 35), (190, 35), (135, 120), (-135, 120)], CONCRETE_LIGHT, CONCRETE_MED, 1)
    # Shadow under the rim
    draw_polygon(t, [(-190, 35), (190, 35), (175, 45), (-175, 45)], CONCRETE_DARK)
    
    # Tier 4: The Roof Peak Cap
    draw_polygon(t, [(-125, 120), (125, 120), (0, 145)], CONCRETE_MED, CONCRETE_DARK, 1)
    
    # ---- 4. Lake Details & Reflections ----
    # Darker structural reflections on the water surface
    draw_filled_rect(t, -140, -90, 280, 25, LAKE_SHADOW)
    # Water ripples
    ripple_data = [(-200, -140, 80), (-50, -120, 110), (120, -160, 70), (-280, -200, 120), (60, -220, 90)]
    for rx, ry, r_width in ripple_data:
        draw_filled_rect(t, rx, ry, r_width, 4, "#5DADE2")
        
    # ---- 5. Foreground Campus Lawn ----
    # Diagonal grassy bank on the bottom left corner
    draw_polygon(t, [(-360, -150), (-110, -360), (-360, -360)], GRASS_GREEN)
    
    # ---- 6. The Famous York Goose ----
    draw_goose(t, -260, -230)
    
    
    #turtle.update()
    screen.mainloop()

if __name__ == "__main__":
    main()