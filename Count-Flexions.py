#Plotting EMG Signal and Counting Flexions

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import filtfilt, butter


File_data = np.loadtxt(".\opensignals_CC78AB5E9D17_2022-05-11_14-58-12.txt", dtype=int)

Amplitude=[]
# print(len(File_data)) 
for i in range (len(File_data)):
    Amplitude.append(File_data[i][5])
# print(Amplitude)
Amplitude=np.array(Amplitude)
x = np.arange(0,len(File_data),1)
# print(max(Amplitude))
fig = plt.figure()
# print(len(x))
plt.plot(x,Amplitude)
plt.show()

#counting flexions
# count points higher than a certain percentile, and use a refractive period to avoid counting the same peak multiple times.
count = 0
threshold = np.percentile(Amplitude,98)
flexions= 0
i = 0
while (i <len(Amplitude)):
    if (Amplitude[i]>=threshold):
        flexions = flexions+1
        i= i + 70
    i = i+1     
print(flexions)