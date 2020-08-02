class Cyclist():
    def __init__(self,mass,p,cda,crr,dte):
        self.mass = mass
        self.p   = p
        self.cda = cda
        self.crr = crr
        self.dte = dte

    def v_cda(self,v):
        if v<15/3.6:
            return self.cda*1.1
        elif v<30/3.6:
            return self.cda
        else:
            return self.cda*0.9
        
    def grad_power(self,G):
        a=0.05 #threshhold gradient
        b=0.25 #uphill power boost
        if G<-a:
            p=0
        elif G<0:
            p=(G+a)/a*self.p
        elif G<a:
            p=self.p*(1+G/a*b)
        else:
            p=self.p*(1+b)
        return self.dte*p

    def __str__(self):
        return "Cyclist: {}kg, {}W, cda{}, crr{}, {}DTE".format(round(self.mass,0),round(self.p,0),round(self.cda,2),round(self.crr,4),round(self.dte,2))

