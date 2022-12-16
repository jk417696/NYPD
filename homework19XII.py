import numpy as np
import os

cwd = os.getcwd()
data = np.load(os.path.join(cwd, "outputs.npy"))

cols = np.shape(data)[1] #number of columns

start = data[:,0] #sizes of structures at the beggining of observation
end = data[:,cols-1] #sizes of structures at the end of observation

doubled = (end/start >= 2)  #checking which structures doubled in size during the observation

new_data = np.c_[data, doubled] #adding a column with information whether the structure doubled in size






