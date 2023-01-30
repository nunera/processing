def setup():
    size(800,600)
    background("#232323")
    noStroke()
    global x
    global wasd
    global y
    x = 400
    y = 400
    wasd = [0,0,0,0]
    
def draw():
    global speed
    global x
    global y
    speed = 4
    siz = 3
    x += (wasd[3]*speed)
    x -= (wasd[1]*speed)
    y += (wasd[2]*speed)
    y -= (wasd[0]*speed)
    if x < -25:
        x = width + 25
    if x > width + 25:
        x = -25
    if y < -25:
        y = height + 25
    if y > height + 25:
        y = -25
    strokeWeight(3)
    stroke(255)
    fill("#A2B1FE")
    circle(x,y,16*siz)

def keyPressed():
    if key == "w":
        wasd[0] = 1
    if key == "a":
        wasd[1] = 1
    if key == "s":
        wasd[2] = 1
    if key == "d":
        wasd[3] = 1
def keyReleased():
    if key == "w":
        wasd[0] = 0
    if key == "a":
        wasd[1] = 0
    if key == "s":
        wasd[2] = 0
    if key == "d":
        wasd[3] = 0
