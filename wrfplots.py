#This program plots WRF output files taking from one output folder. And plotting it with shapefile.

@author : chandrima chakrabarty (chakrabartychandrima91@gmail.com)



#!/usr/bin/env python
# coding: utf-8

# In[72]:


from netCDF4 import Dataset
from matplotlib import cm


# In[2]:


import numpy as np


# In[3]:


wrf_nc_file = 'F:/chandrima/WRF/plots/3B42_month_clim.nc'


# In[4]:


fh = Dataset(wrf_nc_file, mode='r')


# In[5]:


fh.variables.keys()


# In[6]:


lons = fh.variables['LON841_1280'][:]
lats = fh.variables['LAT121_380'][:]
rain = fh.variables['HQPRECIPITATION'][:]
rain_units = fh.variables['HQPRECIPITATION'].units


# In[7]:


fh.close()


# !conda install -c anaconda basemap

# !sudo apt-get install libgeos-3.5.0
# !sudo apt-get install libgeos-dev
# !sudo pip install https://github.com/matplotlib/basemap/archive/master.zip

# In[18]:


import os


# In[22]:


os.environ['PROJ_LIB'] = 'C:/Users/android1/Anaconda3/pkgs/basemap-1.2.1-py37h79c95a4_1/Library/share/basemap'


# In[23]:


import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


# In[24]:


lon_0 = lons.mean()
lat_0 = lats.mean()


# In[83]:



m = Basemap(resolution='c',projection='merc',llcrnrlat=0,urcrnrlat=40,llcrnrlon=60,urcrnrlon=110)


# In[63]:


lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon, lat)


# In[64]:


rain.shape


# In[93]:


plt.figure(figsize=[20,10])
#m.drawcoastlines()
#m.drawstates()
#m.drawcountries()
#m.readshapefile('F:/chandrima/GIS/shape fils/india-soi15420715/shapefile_india/india-soi154207','INDIA')
m.readshapefile('F:\chandrima\GIS\shape fils\india-soi15420715\india_state_shapefile/admin2','state')
cs = m.pcolor(xi,yi,rain[7,:,:],cmap=cm.gist_rainbow_r)
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(rain_units)
plt.title('DJF Maximum Temperature')
plt.show()
plt.savefig('F:/chandrima/WRF/plots/demo.jpg')


# In[ ]:




