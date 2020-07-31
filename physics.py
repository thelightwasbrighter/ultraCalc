import math

g = 9.81

def Cda(Cd,A):
    return Cd*A

def Frr(Crr,G,m):
    return Crr*math.cos(math.atan(G/100.0))*m*g

def Fgrav(G,m):
    return math.sin(math.atan(G/100.0))*m*g

def Fda(Cda,rho,v):
    return 0.5*Cda*rho*v**2

def Fbwd(Crr,Cda,G,m,rho,v):
    return Frr(Crr,G,m) + Fgrav(G,m) + Fda(Cda,rho,v)

def Prr(Crr,G,m,v):
    return Frr(Crr,G,m)*v

def Pgrav(G,m,v):
    return Fgrav(G,m)*v

def Pda(Cda,rho,v):
    return Fda(Cda,rho,v)*v

def Pbwd(Crr,Cda,G,m,rho,v):
    return Fbwd(Crr,Cda,G,m,rho,v)*v

def Ffwd(Pfwd,v):
    return Pfwd/v

def Fres(Pfwd,Crr,Cda,G,m,rho,v):
    return Ffwd(Pfwd,v)-Fbwd(Crr,Cda,G,m,rho,v)

