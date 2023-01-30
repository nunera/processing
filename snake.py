def setup():
    background("#232323")
    size(500,500)
    global bounds
    bounds = [500,500]
    global dir
    dir = "NONE"
    global plus
    plus = 0
    global turnPoint
    turnPoint = [100,0]
    
def draw():
    print(turnPoint)
    global dir
    print(dir)
    speed = 50 
    leng = 1000
    global m
    m = millis()    
    fast = (500/speed) 
    headspeed = (m+leng)/fast
    tailspeed = m/fast
    global dir
    if dir == "down":
        global head
        head = [turnPoint[0],headspeed]
        global tail
        tail = [turnPoint[0],tailspeed] 
    elif dir == "left":
        global head
        head = [headspeed,turnPoint[1]]
        global tail
        tail = [tailspeed,turnPoint[1]]
    elif dir == "right":
        global head
        head = [headspeed,turnPoint[1]]
        global tail
        tail = [tailspeed,turnPoint[1]]
        print("uh")
    elif dir == "up":
        global head
        head = [turnPoint[0],headspeed]
        global tail
        tail = [turnPoint[0],tailspeed]
    else:
        dir = "down"
        head = [turnPoint[0],headspeed]
        global tail
        tail = [turnPoint[0],tailspeed]  
    if head[0] > bounds[0] or head[0] < 0 or head[1] > bounds[1] or head[1] < 0:
        exit()
    fill("#232323")
    rect(0+1,0+1,bounds[0]-3,bounds[1]-3)
    stroke(255)
    line(head[0],head[1],tail[0],tail[1]) 
    
def keyPressed():
    global dir
    if dir == "NONE":
        global dir
        dir = "down"
    if key == CODED:
        if keyCode == UP:
            if not (dir == "down" or dir == "up"):
                global turnPoint
                turnPoint = head
                global dir
                dir = "up"
                global plus
                plus = m
        elif keyCode == RIGHT:
            if not (dir == "left" or dir == "right"):
                global turnPoint
                turnPoint = head
                global dir
                dir = "right"
                global plus
                plus = m
        elif keyCode == DOWN:
            if not (dir == "down" or dir == "up"):
                global turnPoint
                turnPoint = head
                global dir
                dir = "down"
                global plus
                plus = m
        elif keyCode == LEFT:
            if not (dir == "left" or dir == "right"):
                global turnPoint
                turnPoint = head
                global dir
                dir = "left"
                global plus
                plus = m
