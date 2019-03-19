def setup():
    global img
    global sup
    size(501, 670)
    background(255)
    img = loadImage("met empty.jpg")
    sup = loadImage("met empty supplement.jpg")


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
            
            tot1 = (r + g + b) / 3
            
            r2 = red(sup.pixels[loc])
            b2 = blue(sup.pixels[loc])
            g2 = green(sup.pixels[loc])
            
            tot2 = (r2 + g2 + b2) / 3
            
            if tot2 > tot1:
                pixels[loc] = color(r2, g2, b2, 175)
            
            else:
                pixels[loc] = color(r, g, b, a)
        
        updatePixels()
    save("met empti.png")
