#!/usr/bin/python
# coding: utf-8

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Set the box borders in latitudes and langitudes
lats = [90,60,30,0,-30,-60,-90]
lons = [-180,-120,-60,0,60,120,180]
# fill in some data for the boxes
data = np.array([[1,0,1,0,1,0],
                 [1,1,1,1,1,1],
                 [2,2,2,2,2,2],
                 [3,3,3,3,3,3],
                 [4,2,4,2,4,2],
                 [4,4,4,4,4,4]])

# data mask, 1 means that data is masked i.e. not plotted
msk  = np.array([[0,0,0,0,0,0],
                 [0,0,1,0,0,0],
                 [1,0,1,0,0,1],
                 [1,0,0,0,1,0],
                 [1,0,1,1,1,0],
                 [0,0,0,0,0,0]],dtype=bool)

data_masked = np.ma.array(data,mask=msk)


# List of possible map projections:
#   http://matplotlib.org/basemap/users/mapsetup.html
m = Basemap(projection='robin',lon_0=0)
X, Y = m(*np.meshgrid(lons, lats))
C = data_masked

# list of colormaps:
# http://matplotlib.org/examples/color/colormaps_reference.html
image1 = m.pcolor(X,Y,C,cmap=plt.get_cmap('viridis'),zorder=2)
m.drawcoastlines(zorder=3)
plt.title('My global data')

plt.savefig('figure4.png',dpi=150)

# About zorder:
# Larger value puts stuff on top of others.
