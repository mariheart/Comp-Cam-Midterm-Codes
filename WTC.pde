PImage img;

void setup() {
  size(1008, 756);
  background(255);
  img = loadImage("WTC.jpg");
}

void draw() {
  for (int y = 0; y < height; y++) {
    for (int x = 0; x < width; x++) {
      int loc = x + y * width;
      
      float r = red(img.pixels[loc]);
      float g = green(img.pixels[loc]);
      float b = blue(img.pixels[loc]);
      
      if (b > 200 || 120 < r && r < 140 || 170 < g && g < 190) {
        noStroke();
        fill(random(200, 255));
        ellipse(x, y, 1, 1);
      } else {
        noStroke();
        fill(g / 4, b / 1.3, r);
        ellipse(x, y, 1, 1);
      }
    }
  }
  updatePixels();
  save("WTC.png");
}
