import numpy as np
import matplotlib.pyplot as plt

# Constants
a0 = 5.29177210903e-11  # Bohr radius in meters

# Radial probability density for the ground state of hydrogen (n=1, l=0)
def radial_probability_density(r):
    return (1 / (np.pi * a0**3)) * np.exp(-2 * r / a0)

# Generate a range of r values
r = np.linspace(0, 10 * a0, 1000)

# Calculate the radial probability density
P_r = radial_probability_density(r)

# Plot the radial probability density
plt.figure(figsize=(10, 6))
plt.plot(r / a0, P_r, label='Radial Probability Density $P(r)$')
plt.xlabel('Radius $r$ ($a_0$)')
plt.ylabel('Probability Density $P(r)$')
plt.title('Radial Probability Density of the Electron in Hydrogen Atom (Ground State)')
plt.legend()
plt.grid(True)
plt.show()
