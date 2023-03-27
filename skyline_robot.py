def building(distance,hight,w,z):
    h = (hight-(z*20))
    fill((z*70-100)%255)
    rect(((-1*(float(1)/z))*time)+distance+800,450-h,w,h)
wasdclick = [0,0,0,0,0]
gamephase = 0
debug = True
# 0 = Main Menu, 1 = Options, 2 = Game, 3 = Game over screen
def setup():
    size(800,500)
    background("#232323")
startTime = 0
m = 0
t = False
circX = 400
speed = 1
def draw():
    global speed
    global t
    global m
    global gamephase
    if gamephase == 0:
        background("#232323")
        noStroke()
        fill(255,255,255)
        textSize(32)
        textAlign(CENTER)
        text("Start",width/2,210)
        text("Settings",width/2,290)
        if wasdclick[4] == 1:
            if mouseX > 360 and mouseY > 185 and mouseX < 440 and mouseY < 220:
               gamephase = 2
            elif mouseX > 345 and mouseY > 260 and mouseX < 460 and mouseY < 300:
                gamephase = 1
    elif gamephase == 1:
        fill("#FFFFFF")
        global circX
        background("#232323")
        textSize(32)
        textAlign(RIGHT)
        text("Start Speed",width/2-75,210)
        fill("#111211")
        circle(width/2-50,200,10)
        rect(width/2-50,195,200,10)
        circle(width/2+150,200,10)
        fill("#FFFFFF")
        circle(circX,200,10)
        textSize(15)
        textAlign(CENTER)
        text(speed,circX,225)
        textSize(32)
        if mouseX > 350 and mouseY > 150 and mouseX < 550 and mouseY < 230 and wasdclick[4] == 1:
            circX = mouseX
            speed = ((mouseX/float(200)) - 1)
        textAlign(CENTER)
        text("Return",width/2,340)
        if mouseX > 345 and mouseY > 310 and mouseX < 460 and mouseY < 350 and wasdclick[4] == 1:
            gamephase = 0
    elif gamephase == 2:
        global time
        background("#232323")
        if t == False:
            t = True
            m = millis()
        time = (millis() - m) * speed
        fill("#B0BEFF")
        rect((-1*time)+800,0,time,time+600) 
        fill("#32801b")
        rect((-1*time)+800,450,time,50)
        fill("#111111")
        building(220,400,100,2.5)
        building(210,200,100,2.25)
        building(200,450,100,2)
        fill("#111111")
        rect(15,10,25,10)
        triangle(15,5,15,25,5,15)
        if mouseX < 50 and mouseY < 50 and wasdclick[4] == 1:
            background("#232323")
            m = 0
            t = False
            gamephase = 0
    if debug:
        textAlign(CENTER)
        textSize(10)
        fill("#FF0000")
        text("%s, %s" % (mouseX,mouseY),width/2,15)        
    
def mousePressed():
    wasdclick[4] = 1
    
def mouseReleased():
    wasdclick[4] = 0
    
def keyPressed():
    if key == "w":
        wasdclick[0] = 1
    elif key == "a":
        wasdclick[1] = 1
    elif key == "s":
        wasdclick[2] = 1
    elif key == "d":
        wasdclick[3] = 1
        
def keyReleased():
    if key == "w":
        wasdclick[0] = 0
    elif key == "a":
        wasdclick[1] = 0
    elif key == "s":
        wasdclick[2] = 0
    elif key == "d":
        wasdclick[3] = 0
