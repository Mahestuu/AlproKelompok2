class peta:
    def __init__(self):
        self.cityList = {}
    
    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":",self.cityList[kota])
        
    def tambahkanKota(self,kota):
        if kota not in self.cityList:
            self.cityList[kota] = []
            return True
        return False
    
    def hapusKota(self,kotaDihapus):
        #cek apakah kota yang ingin dihapus ada di list
        if kotaDihapus in self.cityList:
        #iterasi setiap kotalain untuk hapus kotadihapus
            for kotalain in self.cityList:
                #cek apakah kota yang ingin dihapus ada jalannya ke kotalain
                if kotaDihapus in self.cityList[kotalain]:
                    self.cityList[kotalain].remove(kotaDihapus)
            del self.cityList[kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #masukkan kota 1 di list kota2
            self.cityList[kota2].append(kota1)
            #masukkan kota 2 di list kota1
            self.cityList[kota1].append(kota2)
            return True
        return False
    
    def hapusJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #hapus kota 1 di list kota2
            self.cityList[kota2].remove(kota1)
            #hapus kota 2 di list kota1
            self.cityList[kota1].remove(kota2)
            return True
        return False
    

petationgkok = peta()
petationgkok.tambahkanKota("xinxiang")
petationgkok.tambahkanKota("jiaozuo")
petationgkok.tambahkanKota("luoyang")
petationgkok.tambahkanKota("pingdingshan")
petationgkok.tambahkanKota("xuchang")
petationgkok.tambahkanKota("luohe")
petationgkok.tambahkanKota("zhoukou")
petationgkok.tambahkanKota("heze")
petationgkok.tambahkanKota("kaifeng")
petationgkok.tambahkanKota("zhengzhou")
print("----------------------------------------------")
petationgkok.tambahkanJalan("xinxiang","jiaozuo")
petationgkok.tambahkanJalan("xinxiang","luoyang")
petationgkok.tambahkanJalan("xinxiang","pingdingshan")
petationgkok.tambahkanJalan("xinxiang","xuchang")
petationgkok.tambahkanJalan("xinxiang","luohe")
petationgkok.tambahkanJalan("xinxiang","zhoukou")
petationgkok.tambahkanJalan("xinxiang","heze")
petationgkok.tambahkanJalan("xinxiang","kaifeng")
petationgkok.tambahkanJalan("xinxiang","zhengzhou")
petationgkok.tambahkanJalan("jiaozuo","luoyang")
petationgkok.tambahkanJalan("jiaozuo","pingdingshan")
petationgkok.tambahkanJalan("jiaozuo","xuchang")
petationgkok.tambahkanJalan("jiaozuo","zhoukou")
petationgkok.tambahkanJalan("jiaozuo","heze")
petationgkok.tambahkanJalan("jiaozuo","kaifeng")
petationgkok.tambahkanJalan("jiaozuo","zhengzhou")
petationgkok.tambahkanJalan("luoyang","pingdingshan")
petationgkok.tambahkanJalan("luoyang","xuchang")
petationgkok.tambahkanJalan("luoyang","luohe")
petationgkok.tambahkanJalan("luoyang","zhoukou")
petationgkok.tambahkanJalan("luoyang","heze")
petationgkok.tambahkanJalan("luoyang","kaifeng")
petationgkok.tambahkanJalan("luoyang","zhengzhou")
petationgkok.tambahkanJalan("pingdingshan","xuchang")
petationgkok.tambahkanJalan("pingdingshan","luohe")
petationgkok.tambahkanJalan("pingdingshan","zhoukou")
petationgkok.tambahkanJalan("pingdingshan","heze")
petationgkok.tambahkanJalan("pingdingshan","kaifeng")
petationgkok.tambahkanJalan("pingdingshan","zhengzhou")
petationgkok.tambahkanJalan("xuchang","luohe")

print("------------------------ OUTPUT AWAL ----------------------")
petationgkok.printPeta()
print("------------------------ OUTPUT SETELAH MENGHAPUS KOTA LUOYANG ----------------------")
petationgkok.hapusKota("luoyang")
petationgkok.printPeta()
print("------------------------ OUTPUT SETELAH MENGHAPUS JALAN XUCHANG & LUOHE ----------------------")
petationgkok.hapusJalan("xuchang","luohe")
petationgkok.printPeta()