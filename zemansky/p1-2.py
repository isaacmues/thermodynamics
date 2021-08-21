problem = """
Problem 1.2.
‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒
The limiting value of the ratio of pressures of a gas at the steam point and at the triple
point of water when the gas is kept at a constant volume is found to be 1.365954. What
is the ideal-gas temperature of the steam point to six significant figures?
"""

solution = """
Solution
‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒
The ideal-gas temperature T is defined by the equation

                         ⎛  P  ⎞
    T = 273.16 K   lim   |‒‒‒‒‒|
                 Pтᴘ ⟶ 0 ⎝ Pтᴘ ⎠ 

Therefore T = {:.6f} K.
"""

T = 273.16 * 1.365954

print(problem)
print(solution.format(T))
