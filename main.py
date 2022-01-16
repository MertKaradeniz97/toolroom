from typing import List
from model import users as UserFile
from model import takim as takimFile
from model import isparcasi as isparcasiFile



def login(username,password):  
    for u in userList:
        if username == u.username and password == u.password:
            print("giris basarili")
            print("hosgeldiniz " + u.name)
            return True,u
            
    print("basarisiz")
    return False

if __name__ == "__main__":
    userList = []
    
    #Giriş parametreleri
    newUser = UserFile.Users()
    newUser2 = UserFile.Users()
    newUser.addUser("mert1997","abcd","mertttttt")
    userList.append(newUser)
    newUser2.addUser("mert1996","abcd","mert")
    userList.append(newUser2)
    
    #Giris Ekrani
    uname=input("kullanici adini girin :")
    password=input("sifrenizi girin :")
    
    
    
    check , currentUser= login(uname,password)    
    if (check):
        
  ##################################
    #is parcasi ve takim parametreleri
        takim1 = takimFile.Takim("takim1","a",15,10)
        takim2 = takimFile.Takim("takim2","b",18,1)
        
        
        isParcasi1 = isparcasiFile.IsPacrasi(newUser,"1","ip1")
        isParcasi1.addTakim(takim1)
        isParcasi1.addTakim(takim2)
        
        newUser.addIsParcasi(isParcasi1)
        
    
     #   for i in range(isParcasi1.getTakimCount()):
     #       print(isParcasi1.getTakim().__getitem__(i).name)
     #       print(isParcasi1.getTakim().__getitem__(i).kod)
     #       print(isParcasi1.getTakim().__getitem__(i).motorNo)
    
    
    #########################################
    #GÖREVLENDİRME
        
        
        #SORGULAR
        #print(newUser.isParcasiList.__getitem__(0).getTakim().__getitem__(0).name)
        #print(isParcasi1.user.name)
        
        print("Tanimli Is Parcasi Listesi : ")
        for i in range(len(currentUser.isParcasiList)):
            print(f"{i}   =>  {currentUser.isParcasiList[i].name}")
            
        index = int(input("Birini secin"))
        
      # print(len(currentUser.isParcasiList[index].getTakim()))
       
        for i in range(len(currentUser.isParcasiList[index].getTakim())):
           print(f"{i}  = >  {currentUser.isParcasiList[index].getTakim()[i].name}")
           
        takimsecimi= int(input("takim seciniz: "))
        
        takim=currentUser.isParcasiList[index].getTakim()[takimsecimi]
        print(f"{takim.name}'ını seçtiniz {takim.motorNo} numaralı motor çalıştı takiminizi aliniz ")
