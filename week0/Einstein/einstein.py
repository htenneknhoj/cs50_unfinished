"""Even if you haven’t studied physics (recently or ever!), you might have heard that 𝐸 =𝑚⁢𝑐2, wherein 𝐸 represents energy (measured in Joules), 
𝑚 represents mass (measured in kilograms), and 𝑐 represents the speed of light (measured approximately as 300000000 meters per second), 
per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent."""

def main():
    mass = int(input(""))
    E = energy(mass)
    print(E)

# return energy in Joules of input (mass)
def energy(mass):
    c2 = 300000000 ** 2
    return mass * c2

main()