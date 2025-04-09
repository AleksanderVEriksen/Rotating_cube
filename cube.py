import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Global variables
size = 5 # size of cube
cube_intervals = 0.1 # speed of rotation (less is more)

# Rotate functions
def rotation_matrix_x(angle):
    return np.array([[1, 0, 0],
                     [0, math.cos(angle), -math.sin(angle)],
                     [0, math.sin(angle), math.cos(angle)]])

def rotation_matrix_y(angle):
    return np.array([[math.cos(angle), 0, math.sin(angle)],
                     [0, 1, 0],
                     [-math.sin(angle), 0, math.cos(angle)]])

def rotation_matrix_z(angle):
    return np.array([[math.cos(angle), -math.sin(angle), 0],
                     [math.sin(angle), math.cos(angle), 0],
                     [0, 0, 1]])

# Cube vertices
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



# Plot
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(projection="3d")


# Set axis limits
ax.set_xlim([-(size+1), (size+1)])
ax.set_ylim([-(size+1), (size+1)])
ax.set_zlim([-(size+1), (size+1)])
ax.set_box_aspect([1, 1, 1])  # Hold proporsjonene like

def update_rotations(frame):
    
    
    # Set axis limits
    ax.clear()
    ax.set_xlim([-(size+1), (size+1)])
    ax.set_ylim([-(size+1), (size+1)])
    ax.set_zlim([-(size+1), (size+1)])
    

    # Rotation angle (in radians)
    angle = math.radians(frame)

    Rz = rotation_matrix_z(angle)
    Ry = rotation_matrix_y(angle)
    Rx = rotation_matrix_x(angle)

    rotated_points = Cube.copy()

    # Apply rotation
    for _ in range(3):  # Roter rundt alle akser (x, y, z)
        rotated_points = np.dot(rotated_points, Rz)
        rotated_points = np.dot(rotated_points, Ry)
        rotated_points = np.dot(rotated_points, Rx)
    
    rotated_Cube = rotated_points
    # Plot vertices
    ax.scatter(rotated_Cube[:, 0], rotated_Cube[:, 1], rotated_Cube[:, 2], c='r', s=100)

    # Plot edges
    for edge in edges:
        p1, p2 = rotated_Cube[edge[0]], rotated_Cube[edge[1]]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], c='b')  # Example: edge(0,1) at angle 0 
                                                                        # rotates from p1:(0,0,0) to p2:(5,0,0)
                                                                        # where 0 represent point 0 in cube (0,0,0) and
                                                                        # 1 represent point 1 in cube(5,0,0)
                                                                        # Plotwise: ax.plot([0,5],[0,0],[0,0], c="b") 
animation = FuncAnimation(fig, update_rotations, frames=np.arange(0,360,2),interval = cube_intervals, repeat=True)
plt.show()
