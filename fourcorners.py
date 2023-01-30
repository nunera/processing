def setup():
    size(800,600)
    fill("#000000")
    rect(0,0,width/2,height/2)
    fill("#FF0000")
    rect(width/2,0,width,height/2)
    fill("#00FF00")
    rect(0,height/2,width/2,height/2)
    fill("#0000FF")
    rect(width/2,height/2,width/2,height/2)
    global rgb
    rgb = [0,0,0]
    
def draw():
    speed = 5
    zone = mouseX//(width/2)+(mouseY//(height/2))+mouseY//(height/2)
    print(zone)
    if zone == 1:
        global rgb
        if rgb[0] < 255:
            global rgb
            rgb[0] += speed
    elif zone == 2:
        if rgb[1] < 255:
            global rgb
            rgb [1] += speed
    elif zone == 3:
        if rgb[2] < 255:
            global rgb
            rgb[2] += speed
    else:
        if rgb[0] > 0:
            global rgb
            rgb[0] -= speed
        if rgb[1] > 0:
            global rgb
            rgb[1] -= speed
        if rgb [2] > 0:  
            global rgb
            rgb[2] -= speed
    fill(rgb[0],rgb[1],rgb[2])
    rect(width/2-100,height/2-100,200,200)
