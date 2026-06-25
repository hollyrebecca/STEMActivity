import turtle as t # this allows you to use all turtle methods through t.methodname


t.color("brown")
t.speed(0)  # 0 is the fastest speed possible


def drawhexagon():
    for i in range(6): # repeat the code 6 times
        t.forward(30)
        t.right(60)

def moveposition():
    t.right(60)
    t.back(30)

def movepositionright():
    t.right(120)
    t.forward(30)
    t.left(60)

while True: # this turtle will draw forever
    for i in range(3):
        for c in ("yellow","gold"):
            t.fillcolor(c)
            t.begin_fill()
            drawhexagon()
            t.end_fill()
            moveposition()
    movepositionright()





t.done()