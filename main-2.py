import random
import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))


class Wheel:
  def __init__(self, sectors):
    self.sectors = sectors
    self.angle = 0
    self.angle_speed = 0
    self.angle_accel = 0
  
  def draw(self):
    x = 300
    y = 300
    
    radius = 200
    
    smoothness = 800
    
    coordinates = []
    for i in range(smoothness+1):
      coordinates.append((x+radius * math.cos(math.radians(360/smoothness*i + self.angle)),y++radius * math.sin(math.radians(360/smoothness*i + self.angle))))
    
    sector = 0
    index = 0
    
    polygons = []
    
    while sector < self.sectors:
      polygon = []
      for i in range(int(smoothness/self.sectors)):
        polygon.append(coordinates[index])
        index += 1
      polygon.append((x,y))
      polygons.append(polygon)
      sector += 1
    for i in range(len(polygons)):
      pygame.draw.polygon(screen, self.chooseColor(i), polygons[i])
    
    pygame.draw.polygon(screen, (0,0,0), [(x,y-radius + 10),(x+10,y-radius-10),(x-10,y-radius-10)])
  
  def chooseColor(self, n):
    colors = [(170,0,0),(170,170,0),(0,170,170),(170,0,170),(0,0,170)]
    
    return colors[n%len(colors)]
  
  def spin(self):
    self.angle_speed = 10 + random.randint(-50,50)/50
    self.angle_accel = -200
  
  def frame(self):
    if self.angle_speed>0:
      self.angle += self.angle_speed
      self.angle = self.angle%360
      
      self.angle_speed += self.angle_accel
    else:
      self.angle_speed = 0
    
    


wheel = Wheel(20)
total_money = 0


word = "pineapple"
guessed = []

for l in word:
  guessed.append("_")


screen.fill((255, 255, 255))
wheel.draw()

pygame.display.flip()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  
  input("what do you want to do?? ready to spin the wheel?")
  print("too bad were spinning it anyway")
  wheel.spin()
  
  while wheel.angle_speed>0:
    screen.fill((255, 255, 255))
    wheel.draw()
    wheel.frame()
    
    
    pygame.time.wait(20)
    
    pygame.display.flip()
  
  
  money = random.randint(-50,200)
  
  print("You got $" + str(money) + ".")
  print("multiply this money by how many letters you get in hangman")
  print("Currently you have " + str(guessed) + " guessed")
  letter = ""
  while not len(letter) == 1:
    letter = input("what is you letter?")
    letter = letter.lower()
    if letter in guessed:
      print("You already guessed that")
      letter = ""
  
  correct = 0
  
  if letter in word:
    for i in range(len(word)):
      if word[i] == letter:
        guessed[i] = letter
        correct += 1
  
  money *= correct
  
  total_money += money
  
  if not "_" in guessed:
    print("You win!!!")
    break
  
  print("you have " + str(guessed) + " guessed")
  
  



print("you ended up with $"+str(total_money)+".")

