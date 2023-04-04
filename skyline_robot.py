# Michael Kryvonis
# Period 10

# Controls:
# Fly - Space
# Interact with buttons - Left Mouse click


def gen():
        # Calls all functions to spawn 2 clouds and 6 buildings
        # Parameters: 
        cloud(200,30,30)
        cloud(0,125,25)
        fill("#111111")
        # Parameters: Distance, Height, Width, Z Axis (how far away are the buildings?)
        building(220,400,100,2.7)
        building(100,300,75,2.5)
        building(410,200,100,2.4)
        building(170,135,100,2.25)
        building(160,450,100,2)
        building(350,450,130,1.5)

def cloud(dis,Height,z):
    noStroke()
    # Without this, clouds would disappear before going under 0 on the X axis.
    distance = dis - 500
    fill("#E6E2F9")
    # The first parameter divides by z, ensuring it slows if its further away, multiplies by time to that it moves, and multiplies by negative one so it goes backwards.
    circle(((-1*(1.0/z)*time)%1600)+distance,100+Height,80)
    circle((((-1*(1.0/z)*time)%1600)+50)+distance,110+Height,80)
    circle((((-1*(1.0/z)*time)%1600)+85)+distance,100+Height,40)
    fill("#B0BEFF")
    # Adds a sky colored rectangle that blocks the bottom of the circles making it look like a cartoony cloud.
    rect(((-1*(1.0/z)*time)%1600)+(distance-50),Height+100,200,50)

def hill(distance,Height,z):
    stroke(0)
    strokeWeight(2)
    h = Height
    fill("#31911a")
    # The first parameter divides by z, ensuring it slows if its further away, multiplies by time to that it moves, and multiplies by negative one so it goes backwards.
    circle(((((-1*(0.2/float(z)))*time)+distance+800)%1600)-400,450-h,400)
def building(distance,Height,w,z,Fill = False):
    stroke(0)
    strokeWeight(2)
    # Makes buildings smaller if further away
    h = (Height-(z*20))
    # Adds the option to add a custom building color if desired
    if Fill == False:
        fill((z*70-100)%255)
    else:
        fill(Fill)
    # The first parameter divides by z, ensuring it slows if its further away, multiplies by time to that it moves, and multiplies by negative one so it goes backwards.
    rect(((((-1*(float(1)/z))*time)+distance+800)%1500)-125,450-h,w,(h+55)-(z*20))
    # Adds windows on the X axis
    for u in range(int(h/30)):
        # Adds windows on the Y axis
        for i in range(w/30):
            fill("#A3eEF8")
            rect(((((-1*(float(1)/z))*time)+distance+810+(i*30))%1500)-125,460-h+(u*30),20,20)
# Table to store if mouse down or space pressed
wasdclick = [0,0]
# 0 = Main Menu, 1 = Options, 2 = Game
gamephase = 0
# Adds a mouse coordinate on the top and expands the speed slider
debug = False
def setup():
    size(800,500)
    background("#232323")
startTime = 0
m = 0
t = False
circX = 400
speed = 1
vel = 100
delta = 0
def draw():
    dog = loadImage("Fijian_Street_Dog_Color.png")
    global speed
    global t
    global m
    global gamephase
    global vel
    global delta
    if gamephase == 0:
        vel = 100
        delta = 0
        background("#232323")
        noStroke()
        fill(255,255,255)
        textSize(32)
        textAlign(CENTER)
        text("Start",width/2,210)
        text("Settings",width/2,290)
        # If button clicked, sends to game phase.
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
        # Checks if mouse is clicking the slider
        if mouseX > 350 and mouseY > 150 and mouseX < 550 and mouseY < 230 and wasdclick[1] == 1:
            # Changes speed to mouseX
            circX = mouseX
            if debug:
                speed = ((mouseX/float(20)) - 19) 
            else:
                speed = ((mouseX/float(200)) - 1)
        textAlign(CENTER)
        text("Return",width/2,340)
        # Return to main menu button
        if mouseX > 345 and mouseY > 310 and mouseX < 460 and mouseY < 350 and wasdclick[1] == 1:
            gamephase = 0
    elif gamephase == 2:
        # Vel = Dog Y Axis
        # Delta = Change in Y Axis
        vel -= delta
        # Accelerates if space down, decelerates if space up
        # delta > value = speed limiter
        if wasdclick[0] == 1 and delta < 15.00:
            # Ensures dog is under 470
            if not(vel < 470):
                delta = 2
            # Dog will increase in delta
            if vel > 55.5:
                delta += 0.2
            elif delta > 0.2:
                    delta = (delta * -1) * 0.5
            else:
                vel = 55.5
        else:
            if not(vel > 33.5):
                delta = -2
            elif vel < 450:
                delta -= 0.2
            elif delta < 0.2:
                    delta = (delta * -1) * 0.5
            else:
                vel = 450 
        global time
        background("#232323")
        # Counter since game start
        if t == False:
            t = True
            m = millis()
        time = (millis() - m) * speed
        # Sky
        fill("#B0BEFF")
        rect((-1*time)+800,0,time,time+600) 
        # Background floor
        fill("#012100")
        noStroke()
        rect((-1*time)+800,385,time,15)
        hill(330,-25,2.5)
        fill("#053100")
        noStroke()
        rect((-1*time)+800,400,time,15)
        hill(760,-75,2.25)
        hill(440,-100,1.75)
        fill("#155102")
        noStroke()
        rect((-1*time)+800,415,time,15)
        hill(670,-30,1.5)
        hill(870,-150,1.5)
        fill("#277014")
        noStroke()
        rect((-1*time)+800,430,time,15)
        hill(440,-125,1.25)
        hill(250,-50,1)
        # Sun
        fill("#FFFFAA")
        circle((((.01)*time)%1600)-125,55,100)
        # Foreground floor
        fill("#32801b")
        noStroke()
        rect((-1*time)+800,445,time,55)
        textAlign(CENTER)
        textSize(22)
        fill("#FFFFFF")
        # Distance counter
        text((str(int(time/100))+" floptometers"),width/2,45)
        gen()
        fill("#00FFAA")
        # Main Subject
        image(dog,-20,(vel-75),500,150)
        # Wall
        fill("#232323")
        noStroke()
        rect((-1*time),0,800,time+800)
        # Return arrow
        fill("#FF0000")
        rect(15,10,25,10)
        triangle(15,5,15,25,5,15)
        if mouseX < 50 and mouseY < 50 and wasdclick[1] == 1:
            background("#232323")
            m = 0
            t = False
            gamephase = 0
    if debug:
        # Mouse coordinates if debug enabled
        textAlign(CENTER)
        textSize(10)
        fill("#FF0000")
        text("%s, %s" % (mouseX,mouseY),width/2,15)        

# Passes mouse and space presses to wasdclick list    
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
