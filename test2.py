import numpy as np
from csv import writer
print("Enter 5 instances of either 1, 0, or -1")
mek = input()
mek2 = mek.split()
mek2 = list(map(int, mek2))
ayaya = np.genfromtxt(r"C:\\Users\User\OneDrive\Documents\Python practice\readfiletest.csv", delimiter=",", dtype='f')
cunny = np.multiply(ayaya, mek2)
echo = np.zeros(cunny.shape)
smh= np.zeros(len(cunny))
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
    echo[x] = dansgame[x]*cunny[x]
finalecho = np.sum(echo,axis=0)
print(finalecho)
with open(r"C:\\Users\User\OneDrive\Documents\Python practice\readfiletest.csv",'a', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(mek2)
    f_object.close
