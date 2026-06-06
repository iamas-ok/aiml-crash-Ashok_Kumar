# Task 8: Build and Inspect NumPy Arrays, then Slice Them

import numpy as np


# Create arrays using different NumPy functions
a1 = np.array([72, 85, 91, 64, 78])
a2 = np.arange(2, 22, 2)
a3 = np.zeros((2, 3), dtype=int)
a4 = np.linspace(20, 30, 6)
a5 = np.array(
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90],
    ]
)

print("Scores array:")
print(a1)

print("\nEven numbers array:")
print(a2)

print("\nZero grid:")
print(a3)

print("\n linspace array:")
print(a4)

print("\nMatrix:")
print(a5)


# Inspect arrays
print("\nInspect scores:")
print("Shape:", a1.shape)
print("Dtype:", a1.dtype)
print("Number of dimensions:", a1.ndim)

print("\nInspect matrix:")
print("Shape:", a5.shape)
print("Dtype:", a5.dtype)
print("Number of dimensions:", a5.ndim)


# Indexing and slicing
print("\nIndexing examples:")
print("First score:", a1[0])
print("Last score using negative index:", a1[-1])
print("Value at row 2, column 3 in matrix:", a5[1, 2])

print("\nSlicing examples:")
print("Middle scores as subarray:", a1[1:4])
print("First two rows of matrix as subarray:")
print(a5[:2, :])
print("Last two columns of matrix as subarray:")
print(a5[:, 1:])
