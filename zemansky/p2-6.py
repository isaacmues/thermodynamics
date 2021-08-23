problem = """
Problem 2.6
‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒
Consider a wire that undergoes an infinitesimal change from an initial equilibrium
state to a final equilibrium state.

(a) Show that the change of tension is equal to

                         A Y
        d𝜏 = -𝛂 A Y dT + ‒‒‒ dL 
                          L

(b) A nickel of cross-sectional area 0.0085 cm² under a tension of 20 N and a
    temperature of 20°C is stretched between two rigid supports 1 m apart. If the
    temperature is reduced to 8°C, what is the final tension? (Note: Assume that 𝛂
    and Y remain constant at the values of 1.33 × 10⁻⁵ K⁻¹ and 2.1 × 10⁶Pa,
    respectively.)
"""

solution = """
Solution
‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒
(a) Let 𝜏 be a function of T and L. Then

             ⎛ ∂𝜏 ⎞      ⎛ ∂𝜏 ⎞
        d𝜏 = ⎜‒‒‒‒⎟ dT + ⎜‒‒‒‒⎟ dL
             ⎝ ∂T ⎠L     ⎝ ∂L ⎠T

    We also have that the linear expansivity is

            1 ⎛ ∂L ⎞
        𝛂 = ‒ ⎜‒‒‒‒⎟
            L ⎝ ∂T ⎠𝜏

    And the isothermal Young's modulus

            L ⎛ ∂𝜏 ⎞
        Y = ‒ ⎜‒‒‒‒⎟
            A ⎝ ∂L ⎠T

    So d𝜏 can be rewritten as

             ⎛ ∂𝜏 ⎞  ⎛ ∂L ⎞      A Y 
        d𝜏 = ⎜‒‒‒‒⎟  ⎜‒‒‒‒⎟ dT + ‒‒‒ dL
             ⎝ ∂L ⎠T ⎝ ∂T ⎠𝜏      L 

                         A Y
           = -𝛂 A Y dT + ‒‒‒ dL 
                          L
(b) We can assume that the length of the wire remains constant; therefore dL = 0.
    Then

        Δ𝜏 = -𝛂 A Y ΔT 

    So the tension at 8°C is {} J.
"""

A = 0.0085e-3
L = 1.0
a = 1.33e-5
Y = 2.1e6
T0 = 20.0 + 273.15
T1 = 8.0 + 273.15
t0 = 20.0

t1 = -a * A * Y  * (T1 - T0) + t0

print(problem)
print(solution.format(t1))
