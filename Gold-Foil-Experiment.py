import random

# Size of the experimental space
size = 100

# Position of the gold foil
gold_foil = (size // 2, size // 2)

# Count of atoms that hit the gold foil
hit_count = 0

# Total number of atoms in the experiment
total_atoms = 10000

for _ in range(total_atoms):
    # Generate a random trajectory for the atom
    trajectory = (random.randint(0, size), random.randint(0, size))

    # If the trajectory hits the gold foil, increment the count
    if trajectory == gold_foil:
        hit_count += 1

print(f"Out of {total_atoms} atoms, {hit_count} hit the gold foil.")
