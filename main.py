import pygame
import math

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Rendering")

black = (0, 0, 0)
white = (255, 255, 255)

running = True

# Function to multiply two matrices
def MatrixMul(matrixA, matrixB):
  # Create a result matrix filled with zeros
  result = [[0 for _ in range(len(matrixB[0]))] for _ in range(len(matrixA))]

  # Perform matrix multiplication
  for row in range(len(matrixA)):
    for col in range(len(matrixB[0])):
      for k in range(len(matrixB)):
        result[row][col] += matrixA[row][k] * matrixB[k][col]

  return result

# Size of the cube
size = 100

# Define the cube's verticese
points = [
  [[-size / 2], [size / 2], [size / 2]],
  [[size / 2], [size / 2], [size / 2]],
  [[size / 2], [-size / 2], [size / 2]],
  [[-size / 2], [-size / 2], [size / 2]],

  [[-size / 2], [size / 2], [-size / 2]],
  [[size / 2], [size / 2], [-size / 2]],
  [[size / 2], [-size / 2], [-size / 2]],
  [[-size / 2], [-size / 2], [-size / 2]],
  ]

# Initial angle
angle = 0.05

# Function to calculate the X-axis rotation matrix
def Xrotation(angle):
  radDegree = angle * math.pi/180 # Convert angle to radians
  return [
  [1, 0, 0],
  [0, math.cos(radDegree), -math.sin(radDegree)],
  [0, math.sin(radDegree), math.cos(radDegree)]
  ]

# Function to calculate the Y-axis rotation matrix
def Yrotation(angle):
  radDegree = angle * math.pi/180 # Convert angle to radians
  return [
  [math.cos(radDegree), -math.sin(radDegree), 0],
  [math.sin(radDegree), math.cos(radDegree), 0],
  [0, 0, 1]
  ]

# Function to calculate the Z-axis rotation matrix
def Zrotation(angle):
  radDegree = angle * math.pi/180 # Convert angle to radians
  return [
  [math.cos(radDegree), 0, math.sin(radDegree)],
  [0,1, 0],
  [-math.sin(radDegree), 0, math.cos(radDegree)]
  ]

# Define the connections (edges) between vertices
connections = [
  (0, 1), (1, 2), (2, 3), (3, 0), # Front face
  (4, 5), (5, 6), (6, 7), (7, 4), # Back face
  (0, 4), (1, 5), (2, 6), (3, 7), # Edges connecting front and back
]

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(black)

  # List to store the rotated and projected points
  rotatedPoints = []

  # Rotate and project each point (vertex) in 3D space
  for point in points:
    # Apply X, Y, and Z rotations
    rotated = MatrixMul(Xrotation(angle), point)
    rotated = MatrixMul(Yrotation(angle), rotated)
    rotated = MatrixMul(Zrotation(angle), rotated)

    # Calculate perspective projection
    z = 200 / (200 - rotated[2][0])
    perspective = [
      [z, 0, 0],
      [0, z, 0],
    ]
    projected = MatrixMul(perspective, rotated) # Apply perspective projection
    rotatedPoints.append(projected) # Save the projected point

    # Displace points to be in the middle of the screen
    pointX = int(projected[0][0] + width//2)
    pointY = int(projected[1][0] + height//2)

    # Draw the point (vertex) as a small circle
    pygame.draw.circle(screen, white, (pointX, pointY), 3)

  # Draw edges between the points
  for start, end in connections:
    startPoint = rotatedPoints[start] # Start vertex
    endPoint = rotatedPoints[end] # End vertex

    # Displace points to be in the middle of the screen
    startX = int(startPoint[0][0] + width//2)
    startY = int(startPoint[1][0] + height//2)
    endX = int(endPoint[0][0] + width//2)
    endY = int(endPoint[1][0] + height//2)

    # Draw the edge as a line
    pygame.draw.line(screen, white, (startX, startY), (endX, endY), 1)

  # Increment the rotation angle for continuous rotation
  angle += 0.05

  pygame.display.flip()

pygame.quit()
