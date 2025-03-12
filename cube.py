import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Rotate functions
def rotate_x(x, y, z, angle):
    cos, sin = math.cos(angle), math.sin(angle)
    ry = y * cos - z * sin  
    rz = y * sin + z * cos
    return x, ry, rz

def rotate_y(x, y, z, angle):
    cos, sin = math.cos(angle), math.sin(angle)
    rx = x * cos + z * sin  
    rz = -x * sin + z * cos
    return rx, y, rz

def rotate_z(x, y, z, angle):
    cos, sin = math.cos(angle), math.sin(angle)
    rx = x * cos - y * sin  
    ry = x * sin + y * cos
    return rx, ry, z

# Cube vertices
size = 5
Cube = np.array([
    [0, 0, 0], [size, 0, 0], [0, size, 0], [size, size, 0], 
    [0, 0, size], [size, 0, size], [0, size, size], [size, size, size]
])

# Cube edges (indices of `Cube` array) 
# Lines to draw from Cube points --> (0,1) means cube[0] to cube[1]
edges = [
    (0,1), (1,5), (5,4), (4,0), # Front square
    (2,3), (3,7), (7,6), (6,2), # Back square
    (0,2), (1,3), (5,7), (4,6)  # Connecting edges
]

# Rotation angle (in radians)
angle = math.radians(0)

# Apply rotation
rotated_Cube = np.array([rotate_x(x, y, z, angle) for x, y, z in Cube])

# Plot
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(projection="3d")

# Plot vertices
ax.scatter(rotated_Cube[:, 0], rotated_Cube[:, 1], rotated_Cube[:, 2], c='r', s=100)

# Plot edges
for edge in edges:
    p1, p2 = rotated_Cube[edge[0]], rotated_Cube[edge[1]]
    print(p1, p2)
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], c='b')  # Example: edge(0,1) at angle 0 
                                                                    # rotates from p1:(0,0,0) to p2:(5,0,0)
                                                                    # where 0 represent point 0 in cube (0,0,0) and
                                                                    # 1 represent point 1 in cube(5,0,0)
                                                                    # Plotwise: ax.plot([0,5],[0,0],[0,0], c="b") 

# Set axis limits
ax.set_xlim([-(size+3), (size+3)])
ax.set_ylim([-(size+3), (size+3)])
ax.set_zlim([-(size+3), (size+3)])

plt.show()
