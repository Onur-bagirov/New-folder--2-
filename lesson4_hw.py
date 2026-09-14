# Task - 1

class Mahni:
    def __init__(self,ad,ifaci,muddet):
        self.ad = ad
        self.ifaci = ifaci
        self.muddet = muddet

    def __str__(self):
        return f"{self.ad} - {self.ifaci} ({self.muddet} san)"


    def __lt__(self, other): # Task - 2
        return self.muddet < other.muddet

    def __repr__(self): # Task - 2 
        return f"{self.ad}({self.muddet})"

class Podcast(Mahni):
    def __init__(self, ad, ifaci, muddet,bolum):
        super().__init__(ad, ifaci, muddet)
        self.bolum = bolum

    def __str__(self):
        return f"{super().__str__()} · bölüm {self.bolum}"


mahni = Mahni("Yellow", "Coldplay", 269)
podcast = Podcast("Kosmos", "Elm saati", 1800, 12)

print(mahni)
print(podcast)

#------------------------------------------------------------------------

# Task - 2

mahnilar = [mahni, Mahni("Numb", "Linkin Park", 185)]
print(sorted(mahnilar))

#------------------------------------------------------------------------

# Task - 3

class TarixMixin: # Bonus
    def elave_olundu(self):
        return f"{self.ad} - əlavə edildi"

class Playlist(TarixMixin):
    def __init__(self,ad,):
        self.ad = ad
        self.mahnilar = []

    def elave_et(self,mahni):
        self.mahnilar.append(mahni)

    def __len__(self):
        return len(self.mahnilar)

    def __contains__(self, ad):
        for mahni in self.mahnilar:
            if mahni.ad == ad:
                return True
        return False

    def __add__(self,other):
        yeni = Playlist(f"{self.ad} + {other.ad}")
        yeni.mahnilar = self.mahnilar + other.mahnilar
        return yeni

pl1 = Playlist("Playlist 1")
pl2 = Playlist("Playlist 2")

pl1.elave_et(mahni)
pl2.elave_et(podcast)

print("Yellow" in pl1)
p1_2 = pl1 + pl2

print(len(p1_2))
print(len(pl1))

print(pl1.elave_olundu())
print(Playlist.__mro__)

#------------------------------------------------------------------------