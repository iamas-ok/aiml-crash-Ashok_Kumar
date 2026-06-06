# Task 9: Use Masking, Broadcasting, and a Similarity Calculation

import numpy as np


def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    return dot_product / (norm_v1 * norm_v2)


# Boolean masking
a1 = np.array([45, 78, 62, 91, 55, 88, 39])
mask = a1 >= 60
filtered_values = a1[mask]

print("Original array:")
print(a1)

print("\nBoolean mask for values >= 60:")
print(mask)

print("\nFiltered values without loops:")
print(filtered_values)


# Broadcasting
a2 = np.array([10, 20, 30, 40])
scaled_array = a2 * 2
offset_array = a2 + 5

print("\nOriginal array for broadcasting:")
print(a2)

print("\nBroadcasted scaling: array * 2")
print(scaled_array)

print("\nBroadcasted offset: array + 5")
print(offset_array)


# Cosine similarity
v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
v3 = np.array([1, 0, 0])
v4 = np.array([0, 1, 0])

similarity_1 = cosine_similarity(v1, v2)
similarity_2 = cosine_similarity(v3, v4)

print("\nCosine similarity examples:")
print("Similarity between v1 and v2:", round(similarity_1, 2))
print("Similarity between v3 and v4:", round(similarity_2, 2))
