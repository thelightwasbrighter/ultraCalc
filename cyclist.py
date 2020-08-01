class Cyclist():
    def __init__(self,mass,p,cda,crr,dte):
        self.mass = mass
        self.p   = p
        self.cda = cda
        self.crr = crr
        self.dte = dte

    def v_cda(self,v):
        if v<10/3.6:
            return self.cda*1.1
        elif v<20/3.6:
            return self.cda
        else:
            return self.cda*0.9
        
    def grad_power(self,G):
        a=0.05
        if G<-a:
            p=0
        elif G<0:
            p=(G+a)/a*self.p
        elif G<a:
            p=self.p+G/a*self.p*0.25
        else:
            p=self.p*1.25
        return self.dte*p

    def __str__(self):
        return "Cyclist: {}kg, {}W, cda{}, crr{}, {}DTE".format(self.mass,self.p,self.cda,self.crr,self.dte)

