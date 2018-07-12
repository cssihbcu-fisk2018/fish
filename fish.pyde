def setup():
    size(400, 400)
    background(255, 255, 255)
    frame(100, 50, 90, 90)
    setColor("red")
    ellipse(200, 200, 50, 50)
    setColor("blue")
    ellipse(300, 300, 50, 50)

def frame(xCoordinate, yCoordinate, frameWidth, frameHeight):
    fill(0, 0, 188)
    rect(xCoordinate, yCoordinate, frameWidth, frameHeight)
    fill(255, 255, 255)
    rect(xCoordinate+20, yCoordinate+20, frameWidth/2, frameHeight/2)

def setColor(colorName):
    if colorName == "red":
        fill(255, 0, 0)
    elif colorName == "blue":
        fill(0, 0, 255)
    elif colorName == "green":
        fill(0, 255, 0)
