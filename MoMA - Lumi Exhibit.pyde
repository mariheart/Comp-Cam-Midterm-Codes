def setup():
    global img
    size(504, 672)
    background(255)
    img = loadImage("met lumi.jpg")


def draw():
    loadPixels()
    img.loadPixels()
    for y in xrange(height):
        for x in xrange(width):
            loc = x + (y * width)
            
            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
            
            if b > 200:
                noStroke()
                fill(r, g, b, 150)
                def mousePressed():
                    ellipse(x, y, mouseX, 10)
                mousePressed()
            
            else:
                noStroke()
                fill(random(r), random(g), random(b))
                ellipse(x, y, 1, 1)
        
    save("met lumiii.png")
    '''
i = second()
s = 0 # counter!
while i > -1:
    if i  == 30:
        save("met lumi 30" + str(s) + ".png")
    
    elif i == 60:
        s += 1
        save("met lumi 60" + str(s) + ".png")
    '''
    
            
        
        
    
