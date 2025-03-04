import numpy as np

# Documentation: https://www.vasp.at/wiki/index.php/POSCAR

def read_vasp_file(filename):
    with open(filename, 'r') as file:
        lines = np.array(file.readlines())

    # Scaling factor
    scaling_factor = float(lines[1].strip())
    print(f"Scaling Factor: {scaling_factor}")

    # Lattice vectors
    lattice_vectors = np.empty((3, 3))
    for i in range(2, 5):
        vector = np.array([float(x) for x in lines[i].split()])
        lattice_vectors[i-2] = scaling_factor * vector

    return lattice_vectors


def calculate_lattice_constants(lattice_vectors):
    a = np.linalg.norm(lattice_vectors[0])
    b = np.linalg.norm(lattice_vectors[1])
    c = np.linalg.norm(lattice_vectors[2])

    cosBC = np.dot(lattice_vectors[1], lattice_vectors[2])/(b * c)  #alpha
    cosAC = np.dot(lattice_vectors[0], lattice_vectors[2])/(a * c)  #beta
    cosAB = np.dot(lattice_vectors[0], lattice_vectors[1])/(a * b)  #gamma

    alpha = np.rad2deg(np.arccos(cosBC))
    beta = np.rad2deg(np.arccos(cosAC))
    gamma = np.rad2deg(np.arccos(cosAB))

    return a, b, c, cosBC, cosAC, cosAB, alpha, beta, gamma


def reciprocal_lattice_vectors(lattice_vectors):
    V = np.dot(lattice_vectors[0], np.cross(lattice_vectors[1], lattice_vectors[2]))

    b1 = (2*np.pi/V)*np.cross(lattice_vectors[1], lattice_vectors[2])
    b2 = (2*np.pi/V)*np.cross(lattice_vectors[2], lattice_vectors[0])
    b3 = (2*np.pi/V)*np.cross(lattice_vectors[0], lattice_vectors[1])

    return b1, b2, b3


filename = 'phl-fe1-fe3.vasp'

try:
    lattice_vectors = read_vasp_file(filename)
    print("Lattice Vectors:")
    for vector in lattice_vectors:
        print(f"{vector}")
    print()

    b1, b2, b3 = reciprocal_lattice_vectors(lattice_vectors)
    print("Reciprocal Lattice Vectors:")
    print(b1, "\t", np.linalg.norm(b1))
    print(b2, "\t", np.linalg.norm(b2))
    print(b3, "\t", np.linalg.norm(b3))
    print()

    a, b, c, cosBC, cosAC, cosAB, alpha, beta, gamma = calculate_lattice_constants(lattice_vectors)
    print("Lattice Constants:")
    print(f"a = {a}, b = {b}, c = {c}")
    print(f"alpha = {alpha}, beta = {beta}, gamma = {gamma}")
    print()

    print(f"cosBC = {cosBC}, cosAC = {cosAC}, cosAB = {cosAB}")

except Exception as e:
    print(f"Error reading .vasp file: {e}")
