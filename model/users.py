from model import isparcasi as ip

class Users:
    def __init__(self):
        self.username=""
        self.password=""
        self.name=""
        self.isParcasiList = []
        
    
    def addUser(self, uname,pw,nm):
        self.username =uname
        self.password = pw
        self.name=nm
    
    def addIsParcasi(self,eklenecekIsParcasi):
        self.isParcasiList.append(eklenecekIsParcasi)
    
    