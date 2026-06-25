import turtle as t # this allows you to use all turtle methods through t.methodname

t.pensize(8) # set the thickness of the pen

# t.teleport(-300,400) # move directly to the specific coordinate without drawing on the way
t.penup()
t.setpos(-100,100)
t.pendown()

# t.fillcolor(blue) # without quotes, Python thinks it's a variable, But we haven't created any variable called blue, so Python gets confused and crashes. The quotes tell Python — this is just a word, a piece of text."
t.fillcolor("blue")
t.begin_fill()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(6):
    t.pencolor(colors[i])
    t.forward(100)
    t.right(60)
#indent: remove indent for each line to see the result
    
# colors = ["red", "blue"]
# for i in range(6):
#     t.pencolor(colors[i % 2])
#     t.forward(100)
#     t.right(60)

# while True: # this turtle will draw forever
#     t.forward(500)
#     t.right(60)


# count = 0
# while count < 6:
#     t.forward(100)
#     t.right(60)
#     count += 1

t.end_fill()

t.done()