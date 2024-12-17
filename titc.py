import numpy as np
import math

def Ln(n,i,t,d=2):
    N = int(n/2)
    phii = 2*i*math.pi/(n+1)
    rho = d*math.pi/(n+1)

    s = 0
    for k in range(1,N+1):
        s += np.cos(k*(t-phii))*np.sin(k*rho)/k

    return 1/(n+1)+2*s/np.pi/d

def TITC(P,t,d=2):
	P = np.array(P)
	n = len(P)

	N = 0
	for i in range(n):
		N += Ln(n-1,i,t,d) * P[i]

	return N


def TITC_curve(P,d=2,resolution=100):
    P = np.array(P)
    n = len(P)
    x = 2*np.pi*np.linspace(0,1,n*resolution,endpoint=False)
    f = np.array([Ln(n-1,0,t,d) for t in x])
    C = np.zeros((n*resolution,2))
    for j in range(n):
        c = np.outer(f,P[j])
        C += c
        if j<n-1:
            f = np.roll(f,resolution)
    return C
