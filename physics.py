import math

g   = 9.81
rho = 1.225

def Cda(Cd,A):
    return Cd*A

def Frr(Crr,G,m):
    return Crr*math.cos(math.atan(G))*m*g

def Fgrav(G,m):
    return math.sin(math.atan(G))*m*g

def Fda(Cda,rho,v):
    return 0.5*Cda*rho*v**2

def Fbwd(Crr,Cda,G,m,rho,v):
    return Frr(Crr,G,m) + Fgrav(G,m) + Fda(Cda,rho,v)

def Ffwd(Pfwd,v):
    return min(1e5,abs(Pfwd/v))

def Fres(Pfwd,Crr,Cda,G,m,rho,v):
    return Ffwd(Pfwd,v)-Fbwd(Crr,Cda,G,m,rho,v)

