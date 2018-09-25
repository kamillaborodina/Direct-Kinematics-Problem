import numpy as np
import math
from Robot import Robot

# Checks if a matrix is a valid rotation matrix.
def isRotationMatrix(R):
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype=R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
    return n < 1e-6


# Calculates rotation matrix to euler angles
# The result is the same as MATLAB except the order
# of the euler angles ( x and z are swapped ).
def rotationMatrixToEulerAngles(R):
    assert (isRotationMatrix(R))

    sy = math.sqrt(R[0, 2] * R[0, 2] + R[1, 2] * R[1, 2])

    singular = sy < 1e-6

    if not singular:
        x = math.atan2(R[1, 2], R[0, 2])
        y = math.atan2(sy, R[2, 2])
        z = math.atan2(R[2, 1], -R[2, 0])
    else:
        x = math.atan2(R[0, 1], R[0, 0])
        y = math.acos(R[2, 2])
        z = 0

    return np.array([x, y, z])


# R = np.matrix('-0.5 - 0; 3 4 0; 0 0 1')
i = 0
R = np.array([[math.cos(i), -math.sin(i), 0],
              [math.sin(i), math.cos(i), 0],
              [0, 0, 1]
              ])

print(rotationMatrixToEulerAngles(R))


