import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 1, 9])
y = np.array([240, 25, 20, 30])

plt.title("Sports Watch Daa")
plt.xlabel("Average Pule")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 10, 110, 115, 12, 125])
y = np.array([240, 250, 260, 270, 280, 290, 30, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Averae Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()
