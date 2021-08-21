import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

problem = """
Problem 1.1
‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒
In the table below, a number in the top row represents the pressure of a gas in the
bulb of a constant-volume gas thermometer (corrected for dead space, thermal
expansion of bulb, etc.) When the bulb is immersed in a water triple-point cell. The
bottom row represents the corresponding readings of pressure when the bulb is
surrounded by a material at a constant unknown temperature. Calculate the ideal-gas
temperature T of thes material. (Use five significant figures.)

Pтᴘ, kPa\t{:6.3f}\t\t{:6.3f}\t\t{:6.3f}\t\t{:6.3f}
P, kPa  \t{:6.3f}\t\t{:6.3f}\t\t{:6.3f}\t\t{:6.3f}
"""

solution = """
Solution
‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒
The ideal-gas temperature T is defined by the equation

                         ⎛  P  ⎞
    T = 273.16 K   lim   |‒‒‒‒‒|
                 Pтᴘ ⟶ 0 ⎝ Pтᴘ ⎠ 

Therefore applying a linear regression to the data gives T = {:5.3f} K.
"""

P_TP = np.array([133.32, 99.992, 66.661, 33.331])
P = np.array([204.69, 153.54, 102.37, 51.190])
T = 273.16 * P / P_TP
reg  = stats.linregress(P_TP, T)

print(problem.format(
        P_TP[0], P_TP[1], P_TP[2], P_TP[3],
        P[0], P[1], P[2], P[3]
        )
)

print(solution.format(reg.intercept))

# For checking the linear regression
#plt.scatter(P_TP, T, c='black')
#plt.plot(P_TP, reg.slope * P_TP + reg.intercept, c='red')
#plt.show()
