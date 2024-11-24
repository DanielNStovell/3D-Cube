import pygame
import math

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Rendering")

black = (0, 0, 0)
white = (255, 255, 255)

running = True

def MatrixMul(matrixA, matrixB):
  result = [[0 for _ in range(len(matrixB[0]))] for _ in range(len(matrixA))]

  for row in range(len(matrixA)):
    for col in range(len(matrixB[0])):
      for k in range(len(matrixB)):
        result[row][col] += matrixA[row][k] * matrixB[k][col]

  return result

distance = 100

points = [
  [[distance / 2], [distance / 2], [0]],
  [[distance / 2], [-distance / 2], [0]],
  [[-distance / 2], [distance / 2], [0]],
  [[-distance / 2], [-distance / 2], [0]]
  ]

angle = 0.1

def Xrotation(angle):
  radDegree = angle * math.pi/180 
  return [
  [1, 0, 0],
  [0, math.cos(radDegree), -math.sin(radDegree)],
  [0, math.sin(radDegree), math.cos(radDegree)]
  ]

def Yrotation(angle):
  radDegree = angle * math.pi/180 
  return [
  [math.cos(radDegree), -math.sin(radDegree), 0],
  [math.sin(radDegree), math.cos(radDegree), 0],
  [0, 0, 1]
  ]

def Zrotation(angle):
  radDegree = angle * math.pi/180 
  return [
  [math.cos(radDegree), 0, math.sin(radDegree)],
  [0,1, 0],
  [-math.sin(radDegree), 0, math.cos(radDegree)]
  ]

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(black)

  temp = []
  for point in points:
    rotated = MatrixMul(Xrotation(angle), point)
    rotated = MatrixMul(Yrotation(angle), rotated)

    temp.append(rotated)

    screen_x = int(rotated[0][0] + width//2)
    screen_y = int(rotated[1][0] + height//2)

    pygame.draw.circle(screen, white, (screen_x, screen_y), 1)

  points = temp

  pygame.display.flip()

pygame.quit()