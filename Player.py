class Player:
    def __init__(self, no, name, team):
        self.no = no
        self.name = name
        self.team = team
        self.sari_kart = 0
        self.kirmizi_kart = 0
        self.gol = 0
        self.asist = 0

    def sari_kart_goster(self, dakika):
        self.sari_kart += 1
        print(f"{dakika}: {self.name} ({self.no}) adlı oyuncu Sarı Kart gördü")

        if self.sari_kart == 2:
            self.kirmizi_kart_goster()

    def kirmizi_kart_goster(self, dakika):
        self.kirmizi_kart += 1
        print(f"{dakika}: {self.name} ({self.no}) adlı oyuncu Kırmızı Kart gördü")

        if self.sari_kart == 2:
            print(f"{dakika}: {self.name} ({self.no}) adlı oyuncu ikinci sarı kart gördüğü için 'Kırmızı Kart'")

    def gol_at(self, dakika):
        self.gol += 1
        self.team.skor_arttır()
        print(f"{dakika}: {self.name} ({self.no}) adlı oyuncu {self.gol}. golünü attı.")
        