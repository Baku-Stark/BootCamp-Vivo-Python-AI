class Passaro:
    def voar(self) -> None:
        print("Voando...")

# FIXME : exemplo ruim de uso de herança para "ganhar" o método voar()
class Avestruz(Passaro):
    def voar(self):
        print("Não está voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()
    
def plano_voo(obj : Passaro):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1) # Voando...
plano_voo(p2) # Não está voando...