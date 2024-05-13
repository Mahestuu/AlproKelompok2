class peta:
    def __init__(self):
        self.listKota = {}
    
    def printPeta(self):
        for kota in self.listKota:
            print(kota, ":", self.listKota[kota])
        
    def tambahkanKota(self, kota):
        if kota not in self.listKota:
            self.listKota[kota] = {}
            return True
        return False
    
    def hapusKota(self, hapusKota):
        if hapusKota in self.listKota:
            for kotaLain in self.listKota:
                if hapusKota in self.listKota[kotaLain]:
                    del self.listKota[kotaLain][hapusKota]
            del self.listKota[hapusKota]
            return True
        return False
    
    def tambahkanJalan(self, kota1, kota2, jarak):
        if kota1 in self.listKota and kota2 in self.listKota:
            self.listKota[kota2][kota1] = jarak, 'KM'
            self.listKota[kota1][kota2] = jarak, 'KM'
            return True
        return False
    
    def hapusJalan(self, kota1, kota2):
        if kota1 in self.listKota and kota2 in self.listKota:
            if kota1 in self.listKota[kota2]:
                del self.listKota[kota2][kota1]
            if kota2 in self.listKota[kota1]:
                del self.listKota[kota1][kota2]
            return True
        return False

    def dijkstra(self, source):
        jarak = {kota: float('inf') for kota in self.listKota}
        jarak[source] = 0

        unvisitedCities = list(self.listKota.keys())
        while unvisitedCities:
            minJarak = float('inf')
            dekatKota = None

            for kota in unvisitedCities:
                if jarak[kota] < minJarak:
                    minJarak = jarak[kota]
                    dekatKota = kota
            unvisitedCities.remove(dekatKota)

            for neighbor, weight in self.listKota[dekatKota].items():
                jarakNeighbor = jarak[dekatKota] + weight[0]
                if jarakNeighbor < jarak[neighbor]:
                    jarak[neighbor] = jarakNeighbor

        return jarak
    

kotationgkok = [
    "Xinxiang",
    "Jiaozuo",
    "Luoyang",
    "Pingdingshan",
    "Xuchang",
    "Luohe",
    "Zhoukou",
    "Heze",
    "Kaifeng",
    "Zhengzhou",
]

print("====== Jalan Yang Terhubung =====")
petationgkok = peta()
petationgkok.tambahkanKota("Xinxiang")
petationgkok.tambahkanKota("Jiaozuo")
petationgkok.tambahkanKota("Luoyang")
petationgkok.tambahkanKota("Pingdingshan")
petationgkok.tambahkanKota("Xuchang")
petationgkok.tambahkanKota("Luohe")
petationgkok.tambahkanKota("Zhoukou")
petationgkok.tambahkanKota("Heze")
petationgkok.tambahkanKota("Kaifeng")
petationgkok.tambahkanKota("Zhengzhou")
print("----------------------------------------------")

edges = [
    ("Zhengzhou", "Kaifeng", 66),
    ("Zhengzhou", "Xuchang", 86),
    ("Zhengzhou", "Xinxiang", 76),
    ("Zhengzhou", "Jiaozuo", 76),
    ("Zhengzhou", "Luoyang", 117),
    ("Zhengzhou", "Kaifeng", 66),
    ("Zhengzhou", "Heze", 193),
    ("Zhengzhou", "Pingdingshan", 132),
    ("Zhengzhou", "Luohe", 141), 
    ("Zhengzhou", "Zhoukou", 187),
    ("Zhengzhou", "Kaifeng", 66),
    ("Kaifeng", "Xuchang", 103),
    ("Kaifeng", "Xinxiang", 78),
    ("Kaifeng", "Jiaozuo", 127)
    ("Kaifeng", "Luoyang", 184),
    ("Kaifeng", "Heze", 129),
    ("Kaifeng", "Pingdingshan", 177),
    ("Kaifeng", "Luohe", 150), 
    ("Kaifeng", "Zhoukou", 154)

]

for edge in edges:
    petationgkok.tambahkanJalan(edge[0], edge[1], edge[2])

petationgkok.printPeta()
print("==============")

jaraksemuakota = petationgkok.dijkstra("Zhengzhou")
print("Jarak Kota Berikut Nya dari Zhengzhou")
for kota, jarak in jaraksemuakota.items():
    print(kota, "adalah", jarak, "KM")