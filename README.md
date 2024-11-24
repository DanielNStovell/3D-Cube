# 3D-Rendering
A simple program that shows you a rotating 3D cube in 2D.

![]([https://github.com/Your_Repository_Name/Your_GIF_Name.gif](https://github.com/DanielNStovell/3D-Rendering/blob/main/3D%20Projection%20Demo.gif))

## Description
I made this in Desmos, but I had trouble changing it from Orthographic to Perspective, so I decided to do it in Python.

To make this cube you need to multiply matrices.
You could use a library but I wanted to program it.

I start off by making an empty matrix `result` and filling it with zeros.
Then I used the matrix multiplying algorithm to get my result.
```py
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

```

Now we need to define the points of the 3D cube.
While doing that, we can decide on the size and initial angle. 

```py
# Size of the cube
size = 100

# Define the cube's vertices
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
```

To rotate the points, we apply the X, Y, and Z rotation matrices. 
Here are the functions for them.
<p>These matrices can be found <a href="https://en.wikipedia.org/wiki/Rotation_matrix" style="color: blue;">here</a>.</p>


```py
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

```

We can use this array to determine which point to connect when we draw the edges. Each number will represent the index.

```py
# Define the connections (edges) between vertices
connections = [
  (0, 1), (1, 2), (2, 3), (3, 0), # Front face
  (4, 5), (5, 6), (6, 7), (7, 4), # Back face
  (0, 4), (1, 5), (2, 6), (3, 7), # Edges connecting front and back
]
```

The main loop handles the rendering and animation of the cube. In each frame, the cube is rotated and redrawn. (EXPLANATION BELOW)

```py
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
```

### First Loop
In the first loop, we iterate through every point and apply our rotations. Because pygame's origin (0,0) is on the top left, we have to slightly offset our points.

```py
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
```

We apply our rotations.

```py
    # Apply X, Y, and Z rotations
    rotated = MatrixMul(Xrotation(angle), point)
    rotated = MatrixMul(Yrotation(angle), rotated)
    rotated = MatrixMul(Zrotation(angle), rotated)
```

Next, we calculate the perspective projection for each point and store them in the `rotatedPoints` array.

```py
    # Calculate perspective projection
    z = 200 / (200 - rotated[2][0])
    perspective = [
      [z, 0, 0],
      [0, z, 0],
    ]
    projected = MatrixMul(perspective, rotated) # Apply perspective projection
    rotatedPoints.append(projected) # Save the projected point
```

Displace the points to give the illusion that the origin is at the center of the screen.

```py
    # Displace points to be in the middle of the screen
    pointX = int(projected[0][0] + width//2)
    pointY = int(projected[1][0] + height//2)
```

Finally draw the points as circles.

```py
    # Draw the point (vertex) as a small circle
    pygame.draw.circle(screen, white, (pointX, pointY), 3)
```

### Second Loop
In the second loop, we use our connections array `connections` to connect our vertexes to form edges.

```py
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
```

The final thing we need to do is increment our angle so the cube will continue to rotate.

```py
# Increment the rotation angle for continuous rotation
angle += 0.05
```
