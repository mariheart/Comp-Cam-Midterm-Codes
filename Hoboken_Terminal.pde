PImage img;

void setup() {
  frameRate(30);
  size(567, 1008);
  background(255);
  img = loadImage("Hoboken Terminal.jpg");
}

void draw() {
  tint(int(random(200, 255)), int(random(200, 255)), int(random(200, 255)), 255);
  image(img, 0, 0, width, height);
  copy(0, int(random(1008)), 567, int(random(20, 50)), 0, int(random(1008)), 567, int(random(20,50)));
  
  //saveFrame("image-######.png");
}
