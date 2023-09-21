import random
def rolar_dado():
    return random.randint(1, 10)

def calcular_multiplicador(resultado):
    
    if resultado < 5:
        return resultado / 5.0
    else:
        return resultado - 5 / 5.0
    
resultado = rolar_dado()
multiplicador = calcular_multiplicador(resultado)

print(f"resultado do dado: {resultado}")
print(f"multiplicador de dano: {multiplicador}")