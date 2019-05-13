def setup():
    global img
    global img2
    global img3
    size(567, 1008)
    background(255)
    img = loadImage("1.jpg")
    img2 = loadImage("2.jpg")
    img3 = loadImage("3.jpg")


def draw():
    loadPixels()
    img.loadPixels()
    for y in xrange(height):
        for x in xrange(width):
            loc = x + (y * width)
            
            r = red(img.pixels[loc])
            b = blue(img.pixels[loc])
            g = green(img.pixels[loc])
            a = alpha(img.pixels[loc])
            
            t1 = (r + g + b) / 3
            
            r2 = red(img2.pixels[loc])
            b2 = blue(img2.pixels[loc])
            g2 = green(img2.pixels[loc])
            a2 = alpha(img2.pixels[loc])
            
            t2 = (r + g + b) / 3
            
            r3 = red(img3.pixels[loc])
            b3 = blue(img3.pixels[loc])
            g3 = green(img3.pixels[loc])
            a3 = alpha(img3.pixels[loc])
            
            t3 = (r + g + b) / 3
            
            if t1 < t2 < t3:
                pixels[loc] = color(r3, g3, b3, 175)
            
            elif t2 < t3 < t1:
                pixels[loc] = color(r, g, b, 175)
            
            elif t3 < t1 < t2:
                pixels[loc] = color(r2, g2, b2, 175)
            
            else:
                pixels[loc] = color(r, g2, b3, random(175, 255))
            
    
    updatePixels()
    save("Trail along 96 Transverse.png")
