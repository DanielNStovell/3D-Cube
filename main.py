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
  [[-distance / 2], [distance / 2], [distance / 2]],
  [[distance / 2], [distance / 2], [distance / 2]],
  [[distance / 2], [-distance / 2], [distance / 2]],
  [[-distance / 2], [-distance / 2], [distance / 2]],

  [[-distance / 2], [distance / 2], [-distance / 2]],
  [[distance / 2], [distance / 2], [-distance / 2]],
  [[distance / 2], [-distance / 2], [-distance / 2]],
  [[-distance / 2], [-distance / 2], [-distance / 2]],
  ]

angle = 0.01

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

connections = [
  (0, 1), (1, 2), (2, 3), (3, 0), # Front
  (4, 5), (5, 6), (6, 7), (7, 4), # Back
  (0, 4), (1, 5), (2, 6), (3, 7), # Connection front & back
]

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(black)

  rotatedPoints = []

  for count, point in enumerate(points):
    rotated = MatrixMul(Xrotation(angle), point)
    rotated = MatrixMul(Yrotation(-angle), rotated)
    rotated = MatrixMul(Zrotation(-angle), rotated)

    rotatedPoints.append(rotated)

    pointX = int(rotated[0][0] + width//2)
    pointY = int(rotated[1][0] + height//2)

    pygame.draw.circle(screen, white, (pointX, pointY), 3)

  for start, end in connections:
    start = points[start]
    end = points[end]

    startX = int(start[0][0] + width//2)
    startY = int(start[1][0] + height//2)
    endX = int(end[0][0] + width//2)
    endY = int(end[1][0] + height//2)

    pygame.draw.line(screen, white, (startX, startY), (endX, endY), 1)

  points = rotatedPoints

  pygame.display.flip()

pygame.quit()