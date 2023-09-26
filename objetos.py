class Arma:
    def __init__(self, dano, ataque):
        self.dano = dano
        self.ataque = ataque
        
    def get_dano(self):
        return self.dano
    
    def get_ataque(self):
        return self.ataque
        
EspadaTal = Arma("Ataque Corte!!!" , 10)
print(EspadaTal.get_dano(), EspadaTal.get_ataque())



A1 = Monster("Nome: sprigaan", 100.0)
print(A1.get_name(),A1.get_life())