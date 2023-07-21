# Kreye yon klas Kwiz ki reprezante yon kwiz endividyèl
class Kwiz:
    def __init__(self, non_kwiz):
        self.non_kwiz = non_kwiz
        self.keksyon = []
        self.repons = []

    def ajoute_keksyon(self, keksyon, chwa):
        # Ajoute yon keksyon ak lis chwa nan kwiz la
        self.keksyon.append(keksyon)
        self.repons.append(chwa)

    def evalye_kwiz(self, repons_itilizatè):
        # Evalye repons itilizatè a epi retounen not la
        not_total = 0
        for i in range(len(self.keksyon)):
            if repons_itilizatè[i] == self.repons[i]:
                not_total += 1
        not_final = (not_total / len(self.keksyon)) * 100
        return not_final

# Kreye yon klas Itilizatè ki genyen enfòmasyon sou itilizatè yo
class Itilizatè:
    def __init__(self, non_itilizatè, modpas):
        self.non_itilizatè = non_itilizatè
        self.modpas = modpas

# Kreye yon list pou stoke tout kwiz yo
kwizyo = []

def kreye_kwiz():
    non_kwiz = input("Antre non kwiz la: ")
    kwiz_nouvo = Kwiz(non_kwiz)
    keksyon = input("Antre keksyon an: ")
    chwa = []
    kontinye_ajoute = True
    while kontinye_ajoute:
        chwa_keksyon = input("Antre yon chwa pou keksyon an (antre '-1' pou sispann ajoute chwa yo): ")
        if chwa_keksyon == "-1":
            kontinye_ajoute = False
        else:
            chwa.append(chwa_keksyon)
    kwiz_nouvo.ajoute_keksyon(keksyon, chwa)
    kwizyo.append(kwiz_nouvo)

def jwe_kwiz(kwiz, itilizatè):
    print("Kwiz:", kwiz.non_kwiz)
    repons_itilizatè = []
    for i in range(len(kwiz.keksyon)):
        print("Kesyon", i+1, ":", kwiz.keksyon[i])
        chwa_itilizatè = input("Antre yon chwa pou kesyon an: ")
        repons_itilizatè.append(chwa_itilizatè)
    not_final = kwiz.evalye_kwiz(repons_itilizatè)
    print("Not final la se:", not_final)

# Egzekite pwogram la
def egzekite_pwogram():
    kontinye = True
    while kontinye:
        print("1. Kreye yon kwiz")
        print("2. Jwe yon kwiz")
        print("3. Kwoke pwogram la")
        chwa_itilizatè = input("Antre yon chwa (1, 2, oswa 3): ")
        if chwa_itilizatè == "1":
            kreye_kwiz()
        elif chwa_itilizatè == "2":
            non_itilizatè = input("Antre non itilizatè a: ")
            modpas = input("Antre modpas la: ")
            itilizatè = Itilizatè(non_itilizatè, modpas)
            for kwiz in kwizyo:
                if kwiz.non_kwiz == itilizatè.modpas:
                    jwe_kwiz(kwiz, itilizatè)
                    break
            else:
                print("Kwiz sa pa egziste.")
        elif chwa_itilizatè == "3":
            kontinye = False
        else:
            print("Mete yon chwa valab.")

# Egzekite pwogram la
egzekite_pwogram()
