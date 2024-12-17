import numpy as np
import matplotlib.pyplot as plt

import titc

fichier = "dolphin.poly"
f = open(fichier, "r")
text = f.read()
f.close()

P = []
for a in text.split("\n"):
    tmp = a.split(" ")
    try:
        P.append(np.array([eval(tmp[0]), eval(tmp[1])]))
    except:
        pass

P = np.array(P)

for i in range(len(P)):
    P[i,-1] = -P[i,-1]

P = np.copy(P)

C = titc.TITC_curve(P)

plt.fill(P[:,0], P[:,1], fill=False)
plt.scatter(P[:,0], P[:,1], color='k', s=5)
plt.fill(C[:,0], C[:,1], fill=False, color='C0')

plt.axis('equal')
plt.show()
