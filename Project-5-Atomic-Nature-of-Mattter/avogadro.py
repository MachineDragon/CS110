import math
import stdio


# Reads in the displacements produced by bead_tracker.py from standard
# input; computes an estimate of Boltzmann's constant and Avogadro's number;
# and writes those estimates to standard output.
def main():
    radialD = []
    while not stdio.isEpty():
        radialD.append(stdio.readFloat())
        self_Diffusion = 0.0
        for r in radialD:
            self_Diffusion = self_Diffusion + (r * 0.175e-6)**2
        self_Diffusion /= (2*len(radialD))
    T = 297
    eta = 9.135e-4
    rho = 0.5e-6
    k = (self_Diffusion * 6 * math.pi * eta * rho) / T
    stdio.writef('Boltzman = %12.6e\n', k)
    avo = 8.31457 / k
    stdio.writef('Avogadro = %12.6e\n', avo)


if __name__ == '__main__':
    main()
