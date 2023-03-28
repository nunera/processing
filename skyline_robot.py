def gen():
        fill("#111111")
        building(220,400,100,2.7)
        building(100,300,75,2.5)
        building(410,200,100,2.4)
        building(170,135,100,2.25)
        building(160,450,100,2)
        building(350,450,130,1.5)

def cloud(dis,Height,z):
    noStroke()
    distance = dis - 500
    fill("#E6E2F9")
    circle(((-1*(1.0/z)*time)%1600)+distance,100+Height,80)
    circle((((-1*(1.0/z)*time)%1600)+50)+distance,110+Height,80)
    circle((((-1*(1.0/z)*time)%1600)+85)+distance,100+Height,40)
    fill("#B0BEFF")
    rect(((-1*(1.0/z)*time)%1600)+(distance-50),Height+100,200,50)

def hill(distance,Height,z):
    stroke(0)
    strokeWeight(2)
    h = Height
    fill("#31911a")
    circle(((((-1*(0.2/float(z)))*time)+distance+800)%1600)-400,450-h,400)
def building(distance,Height,w,z):
    stroke(0)
    strokeWeight(2)
    h = (Height-(z*20))
    fill((z*70-100)%255)
    rect(((((-1*(float(1)/z))*time)+distance+800)%1500)-125,450-h,w,(h+55)-(z*20))
    for u in range(int(h/30)):
        for i in range(w/30):
            fill("#A3eEF8")
            rect(((((-1*(float(1)/z))*time)+distance+810+(i*30))%1500)-125,460-h+(u*30),20,20)
wasdclick = [0,0]
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
        if wasdclick[1] == 1:
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
        if mouseX > 350 and mouseY > 150 and mouseX < 550 and mouseY < 230 and wasdclick[1] == 1:
            circX = mouseX
            if debug:
                speed = ((mouseX/float(20)) - 19) 
            else:
                speed = ((mouseX/float(200)) - 1)
        textAlign(CENTER)
        text("Return",width/2,340)
        if mouseX > 345 and mouseY > 310 and mouseX < 460 and mouseY < 350 and wasdclick[1] == 1:
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
        cloud(200,0,20)
        cloud(0,100,15)
        hill(330,-25,2.5)
        hill(760,-75,2.25)
        hill(440,-100,1.75)
        hill(670,-30,1.5)
        hill(870,-150,1.5)
        hill(440,-125,1.25)
        hill(250,-50,1)
        fill("#232323")
        rect((-1*time),0,800,time+800)
        fill("#32801b")
        rect((-1*time)+800,450,time,50)
        gen()
        fill("#111111")
        rect(15,10,25,10)
        triangle(15,5,15,25,5,15)
        if mouseX < 50 and mouseY < 50 and wasdclick[1] == 1:
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
    wasdclick[1] = 1
    
def mouseReleased():
    wasdclick[1] = 0
    
def keyPressed():
    if key == " ":
        wasdclick[0] = 1
        
def keyReleased():
    if key == " ":
        wasdclick[0] = 0
