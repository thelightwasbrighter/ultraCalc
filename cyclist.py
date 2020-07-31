class Cyclist():
    def __init__(self,mass,p,cda,crr,dte):
        self.mass = mass
        self.p   = p
        self.cda = cda
        self.crr = crr
        self.dte = dte

    def __str__(self):
        return "Cyclist: {}kg, {}W, cda{}, crr{}, {}DTE".format(self.mass,self.p,self.cda,self.crr,self.dte)

peter = Cyclist(88+15,
                200,
                0.38,
                0.003448,
                0.95)
