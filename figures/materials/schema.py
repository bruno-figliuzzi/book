# -*- Encoding: Latin-1 -*-
#!/usr/bin/python

import sys, time, os
from os.path import expanduser
home = expanduser("~")

from math import *
import numpy as np
import matplotlib.pyplot as plt

# Data

data = np.zeros((6, 8))
data[1, 7] = 1
data[2, 2:4] += 1
data[2, 5:] += 1
data[3, 0] = 1
data[3, 2:] += 1
data[4, :] += 1
data[5, :] += 1

x0 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7])
y0 = np.array([3, 4, 3, 2, 2, 3, 2, 2, 1])

x1 = np.array([0, 2, 3, 5, 7])
y1 = np.array([3, 3, 2, 2, 1])

x2 = np.array([0, 3, 7])
y2 = np.array([3, 2, 1])

x3 = np.array([0, 7])
y3 = np.array([3, 1])

x = [x0, x1, x2, x3]
y = [y0, y1, y2, y3]

# Plot
fig, ax = plt.subplots(1, 1, figsize=(6, 6), sharex=True, sharey=True, subplot_kw={'adjustable': 'box-forced'})

ax.imshow(data, interpolation='none', vmin=0, vmax=1, aspect='equal', cmap = 'seismic')
ax = plt.gca()
ax.set_xticks(np.arange(-0.5, 8, 1))
ax.set_yticks(np.arange(-0.5, 6, 1))
ax.set_xticklabels(np.arange(-0.5, 8, 1), minor = True)
ax.set_yticklabels(np.arange(-0.5, 6, 1), minor = True)
#ax.plot(x2, y2, linestyle='--', linewidth=2, color = 'yellow')
ax.plot(x0, y0, linewidth=10, color = 'yellow')
ax.grid(color='lightgrey', linestyle='-', linewidth=3)

for tic in ax.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False
    tic.label1On = tic.label2On = False

for tic in ax.yaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False
    tic.label1On = tic.label2On = False

plt.savefig("Schema0.png")

