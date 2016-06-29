#!/usr/bin/python
# coding: utf-8

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

# List of possible map projections:
#   http://matplotlib.org/basemap/users/mapsetup.html
m = Basemap(projection='robin',lat_0=0,lon_0=0)
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')

# draw parallels and meridians.
m.drawparallels(np.arange(-90.,120.,30.))
m.drawmeridians(np.arange(0.,360.,60.))

m.drawmapboundary(fill_color='aqua')

plt.title("My Global Map")

# plt.show()
plt.savefig('figure1.png',dpi=150)

