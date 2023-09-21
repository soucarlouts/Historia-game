import random

dano_fixo = 10

def rolar_dado():
    return random.randint(1, 10)

def calcular_multiplicador(resultado):
    
    if resultado < 5:
        return resultado / 5.0
    else:
        return resultado - 5 / 5.0
    
resultado = rolar_dado()
multiplicador = calcular_multiplicador(resultado)
dano_total = dano_fixo + (dano_fixo * multiplicador)

print(f"resultado do dado: {resultado}")
print(f"multiplicador de dano: {multiplicador}")
print(f"dano total é: {dano_total}")