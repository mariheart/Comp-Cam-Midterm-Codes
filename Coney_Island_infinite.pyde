
def setup():
    global img
    size(672, 504)
    background(255)
    img = loadImage("coney isle.jpg")


def draw():
    loadPixels()
    img.loadPixels()
    for y in xrange(height):
        for x in xrange(width):
            loc = x + (y * width)
            
            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
            
            grey = (r + g + b) / 3
            
            if b >= 173 and not (r > 240 and g > 190):
                pixels[loc] = color(random(255))
            
            else:
                pixels[loc] = color(r / 4, g / 3, b / 2)
    
    
    i = second()
    updatePixels()
    save("coney glitch" + str(i) + ".png")
