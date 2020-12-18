import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

N=11

dataframes = [pd.DataFrame({"x":np.sort(np.random.rand(10)*100),
                            "y1":np.random.rand(10)*30,
                            "y2":np.random.rand(10)*30}) for _ in range(N)]

fig = plt.figure()
ax = plt.axes(xlim=(0,100), ylim=(0,30))

lines = [plt.plot([], [])[0] for _ in range(2)]

def animate(i):
    lines[0].set_data(dataframes[i]["x"], dataframes[i]["y1"])
    lines[1].set_data(dataframes[i]["x"], dataframes[i]["y2"])
    return lines

anim = ani.FuncAnimation(fig, animate, 
           frames=N, interval=20, blit=True)

plt.show()