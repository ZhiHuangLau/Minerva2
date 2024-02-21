import numpy as np
from csv import writer
import matplotlib.pyplot as plt
print("Enter 5 instances of either 1, 0, or -1")
mek = input()
mek2 = mek.split()
print(len(mek2))
mek2 = list(map(int, mek2))
ayaya = np.genfromtxt(r"C:\\Users\User\OneDrive\Documents\Python practice\readfiletest.csv", delimiter=",", dtype='f')
cunny = np.multiply(ayaya, mek2)
print(cunny)
echo = np.zeros(cunny.shape)
smh= np.zeros(len(cunny))
barx = np.linspace(1, len(mek2), len(mek2))
for x in range(len(cunny)):
    duh=0
    for y in range(len(mek2)):
        if mek2[y] or ayaya[x,y] != 0:
            duh = duh + 1      
    smh[x] = (np.sum(cunny[x])) /duh
dansgame = smh**3
print(dansgame)
intensity = np.sum(dansgame)
for x in range(len(cunny)):
    echo[x] = dansgame[x]*ayaya[x]
#print(echo)
echo2 = np.sum(echo,axis=0)

def normalize(arr, t_min, t_max):
    norm_arr = []
    diff = t_max - t_min
    diff_arr = max(arr) - min(arr)    
    for i in arr:
        temp = (((i - min(arr))*diff)/diff_arr) + t_min
        norm_arr.append(temp)
    return norm_arr

finalecho= normalize(echo2, -1, 1)

with open(r"C:\\Users\User\OneDrive\Documents\Python practice\readfiletest.csv",'a', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(mek2)
    f_object.close
plt.figure()
plt.bar(barx, finalecho, width=1)
plt.axhline(y=0,linewidth=1, color='k')
plt.ylim(-1,1)
plt.show()
