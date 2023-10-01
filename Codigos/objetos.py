import random

class Ataque:
    def __init__(self, tipo, dano_fixo, multiplicador_min, multiplicador_max):
        self.tipo = tipo
        self.dano_fixo = dano_fixo
        self.multiplicador_min = multiplicador_min
        self.multiplicador_max = multiplicador_max

    def calcular_dano(self):
        resultado = rolar_dado()
        multiplicador = calcular_multiplicador(resultado)
        dano_total = self.dano_fixo + (self.dano_fixo * multiplicador)
        return dano_total

def rolar_dado():
    return random.randint(1, 10)

def calcular_multiplicador(resultado):
    if resultado < 5:
        return resultado / 5.0
    else:
        return (resultado - 5) / 5.0

class Personagem:
    def __init__(self, nome, pv, pa):
        self.nome = nome
        self.pv = pv
        self.pa = pa

    def atacar(self, alvo, tipo_ataque):
        ataque_escolhido = ataques_disponiveis[tipo_ataque]
        dano_total = ataque_escolhido.calcular_dano()
        print(f"{self.nome} ataca {alvo.nome} com {tipo_ataque}!")
        alvo.receber_dano(dano_total)
        
    def receber_dano(self, dano):
        self.pv -= dano
        if self.pv < 0:
            self.pv = 0
        print(f"{self.nome} recebe {dano} de dano. PV do {self.nome} restante: {self.pv}")

danos_fixos = {
    "C": 10,
    "CR": 5,
    "CP": 15,
}

ataques_disponiveis = {}
for tipo, valor in danos_fixos.items():
    multiplicador_min = 1.0
    multiplicador_max = 2.0
    ataque = Ataque(tipo, valor, multiplicador_min, multiplicador_max)
    ataques_disponiveis[tipo] = ataque

print("Ataques Disponíveis:")
for tipo, ataque in ataques_disponiveis.items():
    print(f"{tipo}: dano fixo {ataque.dano_fixo}")

P1 = Personagem("Heroi", 100, 20)
P2 = Personagem("Monstro", 80, 15)

while P1.pv > 0 and P2.pv > 0:
    tipo_ataque_escolhido = input(f"escolha seu ataque (C/CR/CP) para {P1.nome}: ")
    
    if tipo_ataque_escolhido in ataques_disponiveis:
        P1.atacar(P2, tipo_ataque_escolhido)
    else:
        print("Tipo de ataque escolhido não está disponível. Digite novamente. ")
        continue
    
    tipo_ataque_monstro = random.choice(list(ataques_disponiveis.keys()))
    P2.atacar(P1, tipo_ataque_monstro)
    
    if P1.pv <= 0:
        print(f"{P1.nome} foi derrotado")
        break
    elif P2.pv <= 0:
        print(f"{P2.nome} foi derrotado")
        break
