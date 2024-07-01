import random

class Futboll:
    def __init__(self, takim1, takim2):
        self.takim1 = takim1
        self.takim2 = takim2
    
    def get_olay(self):
        olaylar = ["Gol", "Korner", "Ofsayt", "Taç", "Sarı Kart", "Kırmızı Kart"]
        oranlar = [0.2, 0.2, 0.2, 0.2, 0.1, 0.1]

        olay = random.choices(olaylar, weights=oranlar, k=1)
        return olay[0]
    
    def get_oyuncu(self, oyuncular):
        oyuncuNo = random.randint(0, 22)
        return oyuncular[oyuncuNo]
    
    def start(self):
        print(f"{self.takim1.name} ile {self.takim2.name} takımları arasında maç başladı!")
        for dakika in range(1, 95):
            if dakika % 5 == 0:
                olay = self.get_olay()
                oyuncu = self.get_oyuncu(self.takim1.oyuncular + self.takim2.oyuncular)

                if (olay == "Gol"):
                    oyuncu.gol_at(dakika)
                elif (olay == "Korner"):
                    print(f"{dakika}: {oyuncu.team.name} takımından {oyuncu.name} Korner kullandı.")
                elif (olay == "Ofsayt"):
                    print(f"{dakika}: {oyuncu.team.name} takımından {oyuncu.name} ofsayt'a yakaladnı.")
                elif (olay == "Taç"):
                    print(f"{dakika}: {oyuncu.team.name} takımından {oyuncu.name} Taç kullandı.")
                elif (olay == "Sarı Kart"):
                    oyuncu.sari_kart_goster(dakika)
                elif (olay == "Kırmızı Kart"):
                    oyuncu.kirmizi_kart_goster(dakika)

        print(f"Maç sonucu: {self.takim1.name} {self.takim1.skor} - {self.takim2.name} {self.takim2.skor} ")

