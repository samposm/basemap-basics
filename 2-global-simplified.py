#!/usr/bin/python
# coding: utf-8

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# List of possible map projections:
#   http://matplotlib.org/basemap/users/mapsetup.html
m = Basemap(projection='robin',lat_0=0,lon_0=0)
m.drawcoastlines()

plt.title("Simple Global Map")

# plt.show()
plt.savefig('figure2.png',dpi=150)

