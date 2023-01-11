import random
import time
def setup():
  size(500,500)
  background("#232323") 
  circles = []
  noStroke()
  circle(250,0,.5)
  circles.append([250,0])
  circle(0,500,.5)
  circles.append([0,500])
  circle(500,500,.5)
  circles.append([500,500])
  fill(255,255,255,0)
  circle(450,450,.5)
  recent = [450,450]
  for i in range(500000):
      new = random.choice(circles)
      x = (recent[0] + new[0])/2
      y = (recent[1] + new[1])/2
      fill(x,y,x*y)
      circle(x,y,.4)
      recent = [x,y]
      
      
      
  

