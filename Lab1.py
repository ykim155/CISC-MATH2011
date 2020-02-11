# 1: a1*n^3 + a2*n^2 + a3*n + a4 and b1*n^3 + b2*n^2 + b3*n + b4

x = 0
y = 0
for n in range(1, 1000):  # loop from 1,999.
    x += (2 * n - 1) ** 2  # using 2n-1 to represent odd numbers instead of 2n+1 to include one.
    y += (2 * n) ** 2  # using 2n to represent even numbers

print(x / n ** 3, y / n ** 3)  # divide by n^3 in order to isolate the cubic term's coefficient.

# we get that a1 is roughly 1.333 which is 4/3.
# we get that b1 is is also roughly 1.333, 4/3.

x = 0
y = 0
for n in range(1, 1000):
    x += (2 * n - 1) ** 2
    y += (2 * n) ** 2

print((x / n ** 2) - (4.0 * n / 3.0), (y / n ** 2) - (
            4.0 * n / 3.0))  # here, I am dividing by n^2 to isolate a2, b2. This leaves us with the term a1*n, b1*n which we subtract.

# we can see that a2 is trending toward 0. we can safely assume that a2 is 0.
# we can see that b2 is trending toward 2. we can safelt assume that b2 is 2.

x = 0
y = 0
for n in range(1, 1000):
    x += (2 * n - 1) ** 2
    y += (2 * n) ** 2

print((x / n) - (4.0 * n ** 2 / 3.0), (y / n) - (4.0 * n ** 2 / 3.0) - (
            2 * n))  # here, I am dividing by n to isolate a3, b3. This leaves a1*n^2, b1*n^2 and b2*n which we subtract.

# we can see that a3 is roughly -0.33333 which is -1/3.
# we can see that b3 is roughly 0.6666 which is 2/3.

x = 0
y = 0
for n in range(1, 1000):
    x += (2 * n - 1) ** 2
    y += (2 * n) ** 2

print(x - (4.0 * n ** 3 / 3.0) + (1.0 * n / 3.0), y - (4.0 * n ** 3 / 3.0) - (2 * n ** 2) - (
            2.0 * n / 3.0))  # here, I am subtracting a1*n^3 and a3*n, b1*n^3 and b2*n^2 and b3*n to isolate a4, b4.

# we can see a4 is really small, going toward 0.
# we can also see b4 is really small, going toward 0.


# 2:
import math

pi = math.pi
sqrt = math.sqrt
actual = 2.0 / pi
calc = 0.0
viete = 1.0
tolerance = 0.00000001  # 1e-8
error = 1
i = 0

while error >= tolerance:
    calc = sqrt(2 + calc)  # this value will be calculated calc within calc will recursively insert sqrted values.
    viete *= calc / 2  # where the actual approx is stored.
    error = abs(actual - viete)  # getting the absolute value of the difference between 2/pi and Viète's approximation.
    i += 1  # counter to keep track of how many values we needed to be within tolerance.

print("It took", i, "iterations for Viète's approximation to be within tolerance.")

# 3:
faces = {'f0': ['v0', 'v5', 'v1'], 'f1': ['v1', 'v5', 'v3', 'v4'], 'f2': ['v0', 'v2', 'v5']}

vertices = {vertex: [] for face in faces for vertex in
            faces[face]}  # creating a dictionary with vertices as the keys and empty lists as the values.
for face in faces:
    for vertex in faces[face]:
        vertices[vertex].append(face)  # filling up the list.

face_keys = list(faces.keys())
face_values = list(faces.values())

edges_frozen = {frozenset(
    (face_values[face][vertex % len(face_values[face])], face_values[face][(vertex + 1) % len(face_values[face])])): []
                for face in range(len(face_values)) for vertex in range(len(face_values[face]))}
# creating a dictionary with edges as frozensets so we can use a container as a key without using a tuple (because order matters with a tuple and that creates duplicates and headaches)

for face in range(len(face_values)):
    for vertex in range(len(face_values[face])):
        edges_frozen[frozenset((face_values[face][vertex % len(face_values[face])],
                                face_values[face][(vertex + 1) % len(face_values[face])]))].append(
            face_keys[face])  # filling up the list.

edge_frozen_keys = list(edges_frozen.keys())
edge_frozen_values = list(edges_frozen.values())

edges = {}
for i in range(len(edges_frozen)):
    edge_frozen_list_keys = [list(i) for i in edge_frozen_keys]
    tup = [tuple(edge_frozen_list_keys[i]) for i in
           range(len(edge_frozen_list_keys))]  # converting frozensets to lists to tuples for neatness' sake
    edges = {tup[i]: edge_frozen_values[i] for i in range(len(edges_frozen))}

print(faces)
print(vertices)
print(edges)
