# 3D-Rendering
A simple program that shows you a rotating 3D cube in 2D.

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

```py
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
```
