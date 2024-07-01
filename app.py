from Team import Team
from Futboll import Futboll

besiktas_oyunculari = [
    'Utku Yuvakuran',
    'Valentin Rosier',
    'Domagoj Vida',
    'Rıdvan Yılmaz',
    'Atiba Hutchinson',
    'Josef de Souza',
    'Necip Uysal',
    'Adem Ljajic',
    'Georges-Kevin N\'Koudou',
    'Can Bozdoğan',
    'Cyle Larin',
    'Vincent Aboubakar',
    'Gökhan Töre',
    'Cyle Larin',
    'Ajdin Hasic',
]

galatasaray_oyunculari = [
    'Fernando Muslera',
    'DeAndre Yedlin',
    'Marcão Teixeira',
    'Marcao',
    'Patrick van Aanholt',
    'Taylan Antalyali',
    'Emre Akbaba',
    'Halil Dervisoglu',
    'Mohamed Elneny',
    'Christian Luyindama',
    'Marcelo Saracchi',
    'Florin Andone',
    'Sofiane Feghouli',
    'Mbaye Diagne',
    'Taylan Antalyali',
]

besiktas_takim = Team("Beşiktaş", besiktas_oyunculari)
galatasaray_takim = Team("Galatasaray", galatasaray_oyunculari)

futboll = Futboll(besiktas_takim, galatasaray_takim)

futboll.start()