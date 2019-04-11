PImage img;

void setup() {
  size(756, 1008);
  background(255);
  img = loadImage("Grove Street.jpg");
}

void draw() {
  loadPixels();
  img.loadPixels();
  
  for (int y = 0; y < height; y++) {
    for (int x = 0; x < width; x++) {
      int loc = x + y * width;
      
      float r = red(img.pixels[loc]);
      float g = green(img.pixels[loc]);
      float b = blue(img.pixels[loc]);
      
      if (150 < r && r < 200 && g >= 100 && b >= 100) {
        pixels[loc] = color(r/6, g, b * 1.5);
      } else if (r < 200 && g < 200 && b < 200) {
        pixels[loc] = color(random(255));
      } else {
        pixels[loc] = color(r, g, b);
      }
    }
  }
  updatePixels();
  save("NewGrove.png");
      
}
