import sympy as sp

problem = """
Problem 1.3
‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒
The resistance R' of a particular carbon resistor obeys the equation
       ________
      / log R'
     / ‒‒‒‒‒‒‒‒ = a + b log R'
    √     T

where a = -1.16 and b = 0.675.
(a) In a liquid helium cryostat, the resistance is found to be exactly 1000 Ω (ohms).
    What is the temperature?
(b) Make a log - log graph of R' against T in the resistance range from 1000 to
    30,000 Ω.
"""

solution = """
Solution
‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒
(a) Solving the equation gives T = {:.2f} K.
(b) I'll omit the graph for the moment.
"""

a = -1.16
b = 0.675
R = 1e3

t = sp.symbols("T", real=True, positive=True)
eq = sp.Eq(sp.log(R, 10) / t, (a + (b * sp.log(R, 10))) ** 2)
T = sp.solve(eq, t)[0]

print(problem)
print(solution.format(T))
