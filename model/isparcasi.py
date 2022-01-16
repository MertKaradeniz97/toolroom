from model import takim

class IsPacrasi:
    def __init__(self,user,kod,name):
        self.name = name
        self.kod = kod
        self.takimSayisi = 0
        self.user= user
        self.takimList=[]
    
        
    def addTakim(self, eklenenTakim):
        self.takimList.append(eklenenTakim)
        self.takimSayisi+=1
    
    
    def getTakimCount(self):
        return self.takimSayisi
    
    def getTakim(self):
        return self.takimList
    
 