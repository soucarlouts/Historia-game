import random

print("Corte = C\n")
print("Corte Rapido = CS\n")
print("Corte Pesado= CP\n")
danos_fixos = {
    "C": 10,
    "CR": 5,
    "CP":15,
}

def rolar_dado():
    return random.randint(1, 10)

def calcular_multiplicador(resultado):
    
    if resultado < 5:
        return resultado / 5.0
    else:
        return resultado - 5 / 5.0
print("Ataques Disponiveis: ")
for tipo, valor in danos_fixos.items():
    print(f"{tipo}: dano fixo {valor}")
        
tipo_ataque_escolhido = input("Escolha Seu Ataque!!! ")

if tipo_ataque_escolhido in danos_fixos:
    dano_fixo = danos_fixos[tipo_ataque_escolhido]
    
    resultado = rolar_dado()
    multiplicador = calcular_multiplicador(resultado)
        
    resultado = rolar_dado()
    multiplicador = calcular_multiplicador(resultado)
    dano_total = dano_fixo + (dano_fixo * multiplicador)

    print(f"resultado do dado: {resultado}")
    print(f"multiplicador de dano: {multiplicador}")
    print(f"ataque escolhido ({tipo_ataque_escolhido})")
    print(f"dano total é: {dano_total}")
else:
    print("Tipo de ataque escolhido não existe")
