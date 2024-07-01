import random
from Player import Player

class Team: 
    def __init__(self, name, oyuncular):
        self.name = name
        self.oyuncular = []
        self.skor = 0
        self.create_team(oyuncular)
    
    def create_team(self, oyuncular):
        for oyuncu in oyuncular:
            oyuncu_no = random.randint(0, 100)
            player = Player(oyuncu_no, oyuncu, self)
            
            self.oyuncular.append(player)

    def skor_arttır(self):
        self.skor += 1
   