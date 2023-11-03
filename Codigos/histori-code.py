import time
import random
import os
import pygame
import keyboard

#90m cinza
#91m vermelho
#92m verde
#93m amarelo
#94m azul
#95m roxo
#96m azul claro
#97m branco

class Arma:
    def __init__(self, dano, ataque):
        self.dano = dano
        self.ataque = ataque

    def get_dano(self):
        return self.dano

    def get_ataque(self):
        return self.ataque


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

EspadaTal = Arma("Ataque Corte!!!" , 10)
pause = 1.0
pause2 = 2.0
pause3 = 3.0
pause4 = 10.0
pause5 = 5.0
armas = None
acessorios = None

#Todas as musicas aqui
SomUnis = 'Som/som_unis.mp3'
SomFase = 'Som/somdefase.mp3'
SomDrusila = 'Som/drusila_audiogame.mp3'
SomDigitado = 'Som/som_digitado.mp3'
SomFinal = 'Som/musica_final.mp3'
SomBatalha = 'Som/musica_batalha.mp3'

def rolar_dado():
    return random.randint(1, 6)
resultado_dados = rolar_dado()
pygame.init()
pygame.mixer.music.load(SomUnis)
pygame.mixer.music.load(SomFase)
pygame.mixer.music.load(SomDrusila)
pygame.mixer.music.play()

def fade_in_text(texto, velocidade):
    for i in range(len(texto)):
        print(texto[i], end='', flush=True)
        time.sleep(velocidade)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def obter_armas_e_acessorios(classe):
    match classe:
        case "Paladino":
            return "Espada", "Armadura", "sua"
        case "Feiticeiro":
            return "Cajado", "Amuleto", "seu"
        case "Arqueiro":
            return "Arco", "Aljava", "seu"
        case _:
            return "Classe não reconhecida", "Acessórios não disponíveis"

print('''           \033[94m                                                           
                      @@@@@@@@@@                @@@@@@@@@@                ##        @@@@@@@@@@                          
                      @@@@@@@@@@            @@@@@@@@@@@@@@@@            @@@@    @@@@@@@@@@@@@@@@@@                      
                      @@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@      @@@@@@@@  @@@@@@@@@@@@@@@@                          
                      @@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@  @@@@@@@@                                  
                      @@@@@@@@@@        @@@@@@@@        @@@@@@@@  @@@@@@@@@@  @@@@@@@@                                  
                      @@@@@@@@@@        @@@@            @@@@@@@@  @@@@@@@@@@  @@@@@@@@@@@@@@                            
                      @@@@@@@@@@        @@              @@@@@@@@  @@@@@@@@@@    @@@@@@@@@@@@@@@@                        
                      @@@@@@@@@@            @@@@        @@@@@@@@  @@@@@@@@@@      @@@@@@@@@@@@@@@@                      
                        @@@@@@@@        @@@@@@@@        @@@@@@@@  @@@@@@@@@@              @@@@@@@@##                    
                        @@@@@@@@@@    @@@@@@@@@@        @@@@@@@@  @@@@@@@@@@                @@@@@@@@                    
                        @@@@@@@@@@@@@@@@@@@@@@          @@@@@@@@  @@@@@@@@@@    @@@@@@@@@@@@@@@@@@                      
                          @@@@@@@@@@@@@@@@@@            @@@@@@@@  @@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@                      
                              @@@@@@@@@@##              @@@@@@@@  @@@@@@@@@@    ##@@@@@@@@@@@@@@ 
                    \033[94m                       
                                                                
''')
pygame.init()
pygame.mixer.music.load(SomUnis)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
time.sleep(pause2)

clear_screen()

pygame.init()
pygame.mixer.music.load(SomDrusila)
pygame.mixer.music.play()
texto = '''\033[91m
 _|       ██████╗ ██████╗ ██╗   ██╗███████╗██╗██╗      █████╗        _|
 _|       ██╔══██╗██╔══██╗██║   ██║██╔════╝██║██║     ██╔══██╗       _|
 _|_/     ██║  ██║██████╔╝██║   ██║███████╗██║██║     ███████║     _/_|   
 _|_/     ██║  ██║██╔══██╗██║   ██║╚════██║██║██║     ██╔══██║     _/_|
 _|_/_/   ██████╔╝██║  ██║╚██████╔╝███████║██║███████╗██║  ██║   _/_/_|
 _|_/_/_/ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝ _/_/_/_|
                          (rpg text game)
            ----------------------------------------------
                   Um mundo mágico de imaginação, 
                com textos que prendem seus jogadores
                    e exploram suas capacidades!\033[91m\n'''
                
velocidade = 0.010
fade_in_text(texto, velocidade)
texto = "\n\033[90mPressione Enter para começar o jogo...\033[0m"
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.03)
input()
pygame.mixer.music.stop()
pygame.quit()

clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\033[93mAncião\033[0m: Oh Olá, como estás nobre guerreiro? diga-me, o que tu procuras? aventura? diversão? batalhas? ouro ou glória? HAHAHAHAHA!!!\n\033[93mAncião\033[0m: Veremos como você se sairá nessas terras traiçoeiras, lute, conquiste e saqueie, mostre a este lugar maldito e agourento do que você é feito!')
def reproduz_som_de_letra(letra):
    if letra.isalpha():
        som_letra.play()
    elif letra.isspace():
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

clear_screen()

print('''\033[91m 
 █████╗     ███████╗██╗      ██████╗ ██████╗ ███████╗███████╗████████╗ █████╗ 
██╔══██╗    ██╔════╝██║     ██╔═══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗
███████║    █████╗  ██║     ██║   ██║██████╔╝█████╗  ███████╗   ██║   ███████║
██╔══██║    ██╔══╝  ██║     ██║   ██║██╔══██╗██╔══╝  ╚════██║   ██║   ██╔══██║
██║  ██║    ██║     ███████╗╚██████╔╝██║  ██║███████╗███████║   ██║   ██║  ██║    
╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
 \033[91m''')
pygame.init()
pygame.mixer.music.load(SomFase)
pygame.mixer.music.play()
input('\n\033[90mPróximo...\033[0m')
clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\033[93mNarrador\033[0m: A grande floresta de drusila, que contem as grandes árvores frutiferas, belas e perfumadas, é um labirinto gigante!\n\033[93mNarrador\033[0m: A única forma de realmente conhecer esta floresta, é morando ou caçando aqui.\n\033[93mNarrador\033[0m: E isso é mostrado pelos ēlifi nome dos nativos élficos da floresta...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[93mNarrador\033[0m: A floresta tem um ecossistema próprio, místico e abriga várias raças diferentes.\n\033[93mNarrador\033[0m: Os ēlifis aqui nascidos eram criados pelos humanos como porcos para o abate...\n\033[93mNarrador\033[0m: Essa prática foi mantida por mais de 3 séculos, e ao decorrer desses anos, os ēlifis criaram um ódio pelos humanos!\n\033[93mNarrador\033[0m: Que no momento, não pode ser simplesmente esquecido...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()

time.sleep(pause)
clear_screen()

print('''\033[91m
      ██████╗     ██╗███╗   ██╗██╗ ██████╗██╗ ██████╗ 
     ██╔═══██╗    ██║████╗  ██║██║██╔════╝██║██╔═══██╗
     ██║   ██║    ██║██╔██╗ ██║██║██║     ██║██║   ██║
     ██║   ██║    ██║██║╚██╗██║██║██║     ██║██║   ██║
     ╚██████╔╝    ██║██║ ╚████║██║╚██████╗██║╚██████╔╝
      ╚═════╝     ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝╚═╝ ╚═════╝ 
\033[91m''')
pygame.init()
pygame.mixer.music.load(SomFase)
pygame.mixer.music.play()
input('\n\033[90mPróximo...\033[0m')
clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\033[95mGarota\033[0m: Oh! Finalmente, você despertou está machucado e essas vestimentas, Ough! fedem, e muito!')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[95mGarota\033[0m: Diga-me qual é o teu nome? ')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
nome = input()
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = (f'\033[95mGarota\033[0m: Pelo que vejo em suas vestimentas parece que servia o exército de drusila!\n\033[95mGarota\033[0m: Mas qual classe você era, {nome}?\n')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()

opcoes_classes = ['Paladino', 'Feiticeiro', 'Arqueiro']

while True:
    texto = ('Escolha uma classe \033[92m(Paladino, Feiticeiro, Arqueiro): \033[0m')
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.05)
        
    classes = input()

    classes = classes.capitalize()

    if classes in opcoes_classes:
        break
    else:
        print('Opção inválida. Por favor, escolha entre Paladino, Feiticeiro ou Arqueiro.')
        continue

clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\033[95mGarota\033[0m: Ah, mas é claro, com essas vestimentas era óbvio!')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = (f'\n\033[95mGarota\033[0m: O que fazes aqui {nome}?')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[94mVocê\033[0m: Eu... eu não me lembro.')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[95mGarota\033[0m: O senhor não se lembra de nada? nada mesmo?')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[94mVocê\033[0m: Só lembro de saber quem sou, mas não de estar aqui, agora...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\033[95mGarota\033[0m: Bom, por enquanto, vamos lavar essas vestimentas e limpar seus ferimentos, você esta na pior...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[94mVocê\033[0m: Quem é você, e por quê esta me ajudando?')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[95mGarota\033[0m: Sou apenas uma garota do campo, o ajudei pois senti que era a coisa certa a se fazer...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[93mNarrador\033[0m: Você se sente grato pela ajuda da garota, deseja agradece-la? ')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

opcao_agr = input().upper()

while True:
    if opcao_agr == "NAO":
        time.sleep(pause)
        pygame.init()
        som_letra = pygame.mixer.Sound(SomDigitado)
        volume_tecla = 0.1
        som_letra.set_volume(volume_tecla)
        texto = "\033[93mNarrador\033[0m: Você fica quieto..."

        def reproduz_som_de_letra(letra):
            if letra.isalpha(): 
                som_letra.play()
            elif letra.isspace(): 
                time.sleep(0.05)

        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
            reproduz_som_de_letra(letra)
        
        pygame.quit()
        break

    elif opcao_agr == "SIM":
        time.sleep(pause)

        pygame.init()
        som_letra = pygame.mixer.Sound(SomDigitado)
        volume_tecla = 0.1
        som_letra.set_volume(volume_tecla)
        texto = "\033[93mNarrador\033[0m: Você agradece pela serventia da garota e se sente bem com isso..."

        def reproduz_som_de_letra(letra):
            if letra.isalpha(): 
                som_letra.play()
            elif letra.isspace(): 
                time.sleep(0.05)

        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
            reproduz_som_de_letra(letra)
        
        pygame.quit()
        time.sleep(pause)
        break
    else:
        time.sleep(pause)
        print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
        continue
time.sleep(pause)

clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[95mGarota\033[0m: Bom, agora que estás indo se limpar, pegue seus equipamentos e armas e dê um trato neles pois estão bem imundos!')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

clear_screen()

classe_escolhida = classes
armas, acessorios, pronome = obter_armas_e_acessorios(classe_escolhida)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = (f'\033[93mNarrador\033[0m: Você pega {pronome} {armas} e limpa com cautela, à marcas e arranhões, mas você segue em frente...\n')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = (f'\033[93mNarrador\033[0m: Você ajusta {pronome} {acessorios} e reflete como tudo isso aconteceu...\n\033[93mNarrador\033[0m: Mas tudo estava tão confuso que você só seguiu ao banheiro para se limpar sem dar muita atenção...\n')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = (f'\033[93mNarrador\033[0m: A mulher estrangeira lava suas vestimentas enquanto você se limpava; quando saiu de seu banho achou suas vestimentas limpas!\n\033[93mNarrador\033[0m: Porem no estado que estavam, eram apenas trapos... \n\033[93mNarrador\033[0m: Mas com apenas {pronome} {armas} e {acessorios} você decide ir em frente.\n\033[93mNarrador\033[0m: Mas antes voce à pede para lhe mostrar onde o achou...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause2)

clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = (f'\033[95mGarota\033[0m: Bom {nome}, depois dessa longa caminhada no bosque só posso lhe trazer até aqui.\n\033[95mGarota\033[0m: Boa sorte e que a luz de \033[4mThalmor\033[0m brilhe sobre ti!')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = (f'\n\033[93mNarrador\033[0m: E assim começa sua jornada, com apenas {pronome} {armas} em mãos e trapos em seu corpo você decide investigar...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

clear_screen()

print('''
      \033[91m
 _|     ███████╗ █████╗ ███████╗███████╗     ██╗     _|
 _|     ██╔════╝██╔══██╗██╔════╝██╔════╝    ███║     _|
 _|     █████╗  ███████║███████╗█████╗      ╚██║     _|
 _|     ██╔══╝  ██╔══██║╚════██║██╔══╝       ██║     _|
 _|     ██║     ██║  ██║███████║███████╗     ██║     _|
 _|     ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═╝     _| 
\033[91m\n''')
pygame.init()
pygame.mixer.music.load(SomFase)
pygame.mixer.music.play()
texto = ("\n\033[90mPressione enter para começar a primeira fase...\033[0m")
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.03) 
input()
pygame.mixer.music.stop()
pygame.quit()
clear_screen()          
      
pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\033[93mNarrador\033[0m: você está na entrada de uma floresta cercada por árvores frutiferas!\n\033[93mNarrador\033[0m: Suas frutas são de cores variadas e exalam o melhor perfume que seu nariz ja sentiu!')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = "\n\033[93mNarrador\033[0m: você está com fome, deseja comer? "
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()

opcao_fome = input().upper()
while True:
    if opcao_fome == "NAO":
        time.sleep(pause)

        pygame.init()
        som_letra = pygame.mixer.Sound(SomDigitado)
        volume_tecla = 0.1
        som_letra.set_volume(volume_tecla)
        texto = "\033[93mNarrador\033[0m: Você decide seguir em frente..."

        def reproduz_som_de_letra(letra):
            if letra.isalpha(): 
                som_letra.play()
            elif letra.isspace(): 
                time.sleep(0.05)

        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
            reproduz_som_de_letra(letra)
        
        pygame.quit()
        break

    elif opcao_fome == "SIM":
        time.sleep(pause)

        pygame.init()
        som_letra = pygame.mixer.Sound(SomDigitado)
        volume_tecla = 0.1
        som_letra.set_volume(volume_tecla)
        texto = ("\033[93mNarrador\033[0m: Você pega uma fruta estranha, aparência de maçã, porem com coloração de madeira. Você a morde, seu suco e sabor o revigoram!")
        def reproduz_som_de_letra(letra):
            if letra.isalpha(): 
                som_letra.play()
            elif letra.isspace(): 
                time.sleep(0.05)

        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
            reproduz_som_de_letra(letra)
        
        pygame.quit()
        break

    print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
    opcao_fome = input("\n\033[93mNarrador\033[0m: você esta com fome, deseja comer? ").upper()

time.sleep(pause)

clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\033[93mNarrador\033[0m: Você olha e caminha mais um pouco ao seu redor e vê marcas de batalha nas árvores.\n\033[93mNarrador\033[0m: O que parecem ser garras, com grandes árvores dilaceradas em volta, você investiga? ')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

opcao_investigar = input().upper()

while True:
    if opcao_investigar == "NAO":
        time.sleep(pause)
        pygame.init()
        som_letra = pygame.mixer.Sound(SomDigitado)
        volume_tecla = 0.1
        som_letra.set_volume(volume_tecla)
        texto = "\033[93mNarrador\033[0m: Você continua a caminhar pela floresta sem dar muita atenção aos detalhes..."

        def reproduz_som_de_letra(letra):
            if letra.isalpha(): 
                som_letra.play()
            elif letra.isspace(): 
                time.sleep(0.05)

        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
            reproduz_som_de_letra(letra)
        
        pygame.quit()
        break

    elif opcao_investigar == "SIM":
        time.sleep(pause)

        pygame.init()
        som_letra = pygame.mixer.Sound(SomDigitado)
        volume_tecla = 0.1
        som_letra.set_volume(volume_tecla)
        texto = "\033[93mNarrador\033[0m: você caminha lentamente pela floresta atentando-se aos detalhes e estragos das madeiras e folhas!"

        def reproduz_som_de_letra(letra):
            if letra.isalpha(): 
                som_letra.play()
            elif letra.isspace(): 
                time.sleep(0.05)

        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
            reproduz_som_de_letra(letra)
        
        pygame.quit()
        time.sleep(pause)
        break
    else:
        time.sleep(pause)
        print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
        continue
time.sleep(pause)
clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = (f'\n\033[93mNarrador\033[0m: Enquanto você caminha pela floresta, ouve pegadas se aproximando, é algo grande!\n\033[93mNarrador\033[0m: Você saca {pronome} {armas} e logo em seguida ouve um grunido que faz seu peito resonar com medo!')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = (f'\n\033[93mNarrador\033[0m: E um enorme urso ensanguentado pula de fora da floresta!\n\033[93mNarrador\033[0m: Em sua pelagem densa à marcas de espadas apenas olhar para tal criatura o enche de medo...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

clear_screen()

print('''\033[91m
██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗  ██╗ █████╗ 
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║  ██║██╔══██╗
██████╔╝███████║   ██║   ███████║██║     ███████║███████║
██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██╔══██║██╔══██║
██████╔╝██║  ██║   ██║   ██║  ██║███████╗██║  ██║██║  ██║
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝\033[91m
          ''')
pygame.init()
pygame.mixer.music.load(SomFase)
pygame.mixer.music.play()
texto = ("\n\033[90mPressione enter para começar a batalha...\033[0m")
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.03) 
input()
pygame.mixer.music.stop()
pygame.quit()

clear_screen()   

pygame.init()
pygame.mixer.music.load(SomBatalha)
pygame.mixer.music.play()

danos_fixos = {
    "ataque direto": 10,
    "ataque rapido": 5,
    "ataque pesado": 15,
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

P1 = Personagem("\033[94mGuerreiro\033[0m", 100, 20)
P2 = Personagem("\033[91mUrso ensanguentado\033[0m", 80, 10)

while P1.pv > 0 and P2.pv > 0:
    tipo_ataque_escolhido = input(f"\033[93mNarrador\033[0m: Escolha e digite um ataque para {P1.nome}: ")
    clear_screen()
    
    if tipo_ataque_escolhido in ataques_disponiveis:
        P1.atacar(P2, tipo_ataque_escolhido)
    else:
        print("\033[93mNarrador\033[0m: Tipo de ataque escolhido não está disponível. Digite novamente. ")
        continue
    
    tipo_ataque_monstro = random.choice(list(ataques_disponiveis.keys()))
    P2.atacar(P1, tipo_ataque_monstro)

    if P1.pv <= 0:
        print(f"\n\033[93mNarrador\033[0m: {P1.nome} foi derrotado, mais cuidado da próxima vez!")
        break
    elif P2.pv <= 0:
        print(f"\n\033[93mNarrador\033[0m: {P2.nome} foi derrotado com êxito!")
        break
pygame.mixer.music.stop()
pygame.quit()
time.sleep(pause2)
clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\033[93mNarrador\033[0m: Neste mesmo instante uma bela e luminosa fada aparece acima de seus olhos e fala com você!')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\033[95mFada\033[0m: Por sorte nesta grande batalha os deuses tiveram piedade de você guerreiro!\n\033[95mFada\033[0m: Pois vi suas ações e não esta nada bom para enfrentar as criaturas maléficas desta terra...\n\033[95mFada\033[0m: Não se acostume com milagres, pois este lugar é traiçoeiro!')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[93mNarrador\033[0m: Ao adentrar mais à floresta você vê um labirinto de árvores.\n\033[93mNarrador\033[0m: Você mal entrou e ja se sente perdido tendo apenas as marcas de garra nas árvores.\n\033[93mNarrador\033[0m: O som ominoso que você ouve ja é o suficiente para sentir o mau agouro que lhe espera, porem, você deve prosseguir...\n\033[93mNarrador\033[0m: Afinal, não é como se lhe sobrasse muita escolha...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\033[93mNarrador\033[0m: Você segue as marcas de forma quase linear.\n\033[93mNarrador\033[0m: Seu coração acompanha seus pés com o peito acelerado. você tem medo do que pode encontrar...\n\033[93mNarrador\033[0m: Seus pensamentos embaralham e sua cabeça o tontea de confusão, você não sabe o que vai achar, ver e encontrar por este lugar maldito...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[93mNarrador\033[0m: Você sente medo, ao adentrar a floresta, você sente um cheiro podre de carne.\n\033[93mNarrador\033[0m: Depois de andar em direção ao cheiro, você vê corpos dilacerados, armaduras que outrorá foram brilhantes e reluzentes...\n\033[93mNarrador\033[0m: Você tampa sua boca e nariz; o local está insuportável...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

clear_screen()

print('''
      \033[91m
 _|     ███████╗ █████╗ ███████╗███████╗    ██████╗     _|
 _|     ██╔════╝██╔══██╗██╔════╝██╔════╝    ╚════██╗    _|
 _|     █████╗  ███████║███████╗█████╗       █████╔╝    _|
 _|     ██╔══╝  ██╔══██║╚════██║██╔══╝      ██╔═══╝     _|
 _|     ██║     ██║  ██║███████║███████╗    ███████╗    _|
 _|     ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝    _|
\033[91m\n''')
pygame.init()
pygame.mixer.music.load(SomFase)
pygame.mixer.music.play()
texto = ("\n\033[90mPressione enter para começar a Segunda fase...\033[0m")
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.03) 
input()
pygame.mixer.music.stop()
pygame.quit()
clear_screen() 

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\033[93mNarrador\033[0m: Uma coisa lhe chama atenção, um envelope de carta perto de um dos corpos, você pega? ')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()

opcao_carta = input().upper()

while True:
    if opcao_carta == "NAO":
        time.sleep(pause)
        pygame.init()
        som_letra = pygame.mixer.Sound(SomDigitado)
        volume_tecla = 0.1
        som_letra.set_volume(volume_tecla)
        texto = "\033[93mNarrador\033[0m: Você não pega a carta..."

        def reproduz_som_de_letra(letra):
            if letra.isalpha(): 
                som_letra.play()
            elif letra.isspace(): 
                time.sleep(0.05)

        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
            reproduz_som_de_letra(letra)
        
        pygame.quit()
        break

    elif opcao_carta == "SIM":
        time.sleep(pause)

        pygame.init()
        som_letra = pygame.mixer.Sound(SomDigitado)
        volume_tecla = 0.1
        som_letra.set_volume(volume_tecla)
        texto = "\033[93mNarrador\033[0m: Você se agacha perto de um dos corpos e pega um envelope vazio.\n\033[93mNarrador\033[0m: Porem não é um envelope comum; a marca de cera, você à reconhece, é da realeza Drusiliana!"

        def reproduz_som_de_letra(letra):
            if letra.isalpha(): 
                som_letra.play()
            elif letra.isspace(): 
                time.sleep(0.05)

        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
            reproduz_som_de_letra(letra)
        
        pygame.quit()
        time.sleep(pause)
        break
    else:
        time.sleep(pause)
        print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
        continue

clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[93mNarrador\033[0m: Após isso, você repara em algo muito incomum em uma das carcaças.\n\033[93mNarrador\033[0m: Você vê aquilo que se assemelha a uma flecha, Você investiga? ')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()

opcao_seta = input().upper()

while True:
    if opcao_seta == "NAO":
        time.sleep(pause)

        pygame.init()
        som_letra = pygame.mixer.Sound(SomDigitado)
        volume_tecla = 0.1
        som_letra.set_volume(volume_tecla)
        texto = ("\033[93mNarrador\033[0m: Você não pega a flecha, porém consegue ouvir o som de uma das árvores gemendo e rangendo.\n\033[93mNarrador\033[0m: Uma árvore viva se revela, você não tem escolha senão lutar...")
        def reproduz_som_de_letra(letra):
            if letra.isalpha(): 
                som_letra.play()
            elif letra.isspace(): 
                time.sleep(0.05)

        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
            reproduz_som_de_letra(letra)
        
        pygame.quit()
        break
    elif opcao_seta == "SIM":
        time.sleep(pause)

        pygame.init()
        som_letra = pygame.mixer.Sound(SomDigitado)
        volume_tecla = 0.1
        som_letra.set_volume(volume_tecla)
        texto = ("\033[93mNarrador\033[0m: Novamente, você se abaixa e pega até então a desconhecida flecha, parece uma flecha comum.\n\033[93mNarrador\033[0m: Você não a reconhece de lugar algum, e à guarda.\n\033[93mNarrador\033[0m: logo após consegue ouvir o som de uma das árvores gemendo e rangendo. Uma árvore viva se revela, você não tem escolha senão lutar...")
        def reproduz_som_de_letra(letra):
            if letra.isalpha(): 
                som_letra.play()
            elif letra.isspace(): 
                time.sleep(0.05)

        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
            reproduz_som_de_letra(letra)
        
        pygame.quit()
        break
    else:
        time.sleep(pause)
        print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
        continue

clear_screen()

print('''\033[91m
██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗  ██╗ █████╗ 
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║  ██║██╔══██╗
██████╔╝███████║   ██║   ███████║██║     ███████║███████║
██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██╔══██║██╔══██║
██████╔╝██║  ██║   ██║   ██║  ██║███████╗██║  ██║██║  ██║
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝\033[91m
          ''')
pygame.init()
pygame.mixer.music.load(SomFase)
pygame.mixer.music.play()
texto = ("\n\033[90mPressione enter para começar a batalha...\033[0m")
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.03) 
input()
pygame.mixer.music.stop()
pygame.quit()

clear_screen() 

pygame.init()
pygame.mixer.music.load(SomBatalha)
pygame.mixer.music.play()

danos_fixos = {
    "ataque direto": 10,
    "ataque rapido": 5,
    "ataque pesado": 15,
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

P1 = Personagem("\033[94mGuerreiro\033[0m", 100, 20)
P2 = Personagem("\033[91mÁrvore viva\033[0m", 80, 10)

while P1.pv > 0 and P2.pv > 0:
    tipo_ataque_escolhido = input(f"\033[93mNarrador\033[0m: Escolha e digite um ataque para {P1.nome}: ")
    clear_screen()
    
    if tipo_ataque_escolhido in ataques_disponiveis:
        P1.atacar(P2, tipo_ataque_escolhido)
    else:
        print("\033[93mNarrador\033[0m: Tipo de ataque escolhido não está disponível. Digite novamente. ")
        continue
    
    tipo_ataque_monstro = random.choice(list(ataques_disponiveis.keys()))
    P2.atacar(P1, tipo_ataque_monstro)

    if P1.pv <= 0:
        print(f"\n\033[93mNarrador\033[0m: {P1.nome} foi derrotado, mais cautela da próxima vez guerreiro!")
        break
    elif P2.pv <= 0:
        print(f"\n\033[93mNarrador\033[0m: {P2.nome} foi derrotada com êxito!")
        break
pygame.mixer.music.stop()
pygame.quit()
time.sleep(pause3)
clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto =('\033[93mNarrador\033[0m: Depois de batalhar com Árvore viva, você vê um homem assustado indo em sua direção...\n\033[93mNarrador\033[0m: Você para e tenta entender o que está acontecendo...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[92mHomem desconhecido\033[0m: Obrigado senhor por nos salvar dessa malígna e maldita árvore viva!\n\033[92mHomem desconhecido\033[0m: Ela assombrava e aterrorizava nosso vilarejo á décadas!\n\033[92mHomem desconhecido\033[0m: Depois que o rei de drusila parou de enviar seus soldados para nos apoiar tudo desabou...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[94mVocê\033[0m: Mas como assim parou de enviar soldados para cá?\n\033[94mVocê\033[0m: A missão e a vontade dele era sempre sevir e proteger todos os vilarejos e o reino dele...\n\033[94mVocê\033[0m: Porque parar assim do nada?')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[92mHomem desconhecido\033[0m: Eu também gostaria de saber nobre guerreiro...\n\033[92mHomem desconhecido\033[0m: Mas o que está acontecendo por agora no reino esta afetando tudo e a todos...')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)
clear_screen()

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\033[93mNarrador\033[0m: Você se assusta ao saber o que está acontecendo no reino, pois você não se lembra de quase nada!\n\033[93mNarrador\033[0m: Mas mesmo assim agora sente que tem um propósito e uma missão para seguir! ')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause)

pygame.init()
som_letra = pygame.mixer.Sound(SomDigitado)
volume_tecla = 0.1
som_letra.set_volume(volume_tecla)
texto = ('\n\033[93mNarrador\033[0m: Você agora decide ir seguir uma longa viagem até o reino de Drusila para ver o que está acontecendo...\n\033[93mNarrador\033[0m: E ver o por quê do rei está agindo e sendo tão mal com seu povo!')
def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)
pygame.quit()
time.sleep(pause2)

clear_screen()

print('''\033[91m   
_|     ███████╗██╗███╗   ███╗    ██████╗  ██████╗     ██████╗ ██████╗  ██████╗      ██╗███████╗████████╗ ██████╗      _|
_|     ██╔════╝██║████╗ ████║    ██╔══██╗██╔═══██╗    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝╚══██╔══╝██╔═══██╗     _|
_|     █████╗  ██║██╔████╔██║    ██║  ██║██║   ██║    ██████╔╝██████╔╝██║   ██║     ██║█████╗     ██║   ██║   ██║     _|
_|     ██╔══╝  ██║██║╚██╔╝██║    ██║  ██║██║   ██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝     ██║   ██║   ██║     _|
_|     ██║     ██║██║ ╚═╝ ██║    ██████╔╝╚██████╔╝    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗   ██║   ╚██████╔╝     _|
_|     ╚═╝     ╚═╝╚═╝     ╚═╝    ╚═════╝  ╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝   ╚═╝    ╚═════╝      _|\033[91m
''')
pygame.init()
pygame.mixer.music.load(SomFinal)
pygame.mixer.music.play()
time.sleep(pause5)

clear_screen()

print('''           \033[94m                                                           
                      @@@@@@@@@@                @@@@@@@@@@                ##        @@@@@@@@@@                          
                      @@@@@@@@@@            @@@@@@@@@@@@@@@@            @@@@    @@@@@@@@@@@@@@@@@@                      
                      @@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@      @@@@@@@@  @@@@@@@@@@@@@@@@                          
                      @@@@@@@@@@        @@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@  @@@@@@@@                                  
                      @@@@@@@@@@        @@@@@@@@        @@@@@@@@  @@@@@@@@@@  @@@@@@@@                                  
                      @@@@@@@@@@        @@@@            @@@@@@@@  @@@@@@@@@@  @@@@@@@@@@@@@@                            
                      @@@@@@@@@@        @@              @@@@@@@@  @@@@@@@@@@    @@@@@@@@@@@@@@@@                        
                      @@@@@@@@@@            @@@@        @@@@@@@@  @@@@@@@@@@      @@@@@@@@@@@@@@@@                      
                        @@@@@@@@        @@@@@@@@        @@@@@@@@  @@@@@@@@@@              @@@@@@@@##                    
                        @@@@@@@@@@    @@@@@@@@@@        @@@@@@@@  @@@@@@@@@@                @@@@@@@@                    
                        @@@@@@@@@@@@@@@@@@@@@@          @@@@@@@@  @@@@@@@@@@    @@@@@@@@@@@@@@@@@@                      
                          @@@@@@@@@@@@@@@@@@            @@@@@@@@  @@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@                      
                              @@@@@@@@@@##              @@@@@@@@  @@@@@@@@@@    ##@@@@@@@@@@@@@@ 
                    \033[94m                       
                                                                
''')
pygame.init()
pygame.mixer.music.load(SomUnis)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
time.sleep(pause2)
input("\n\033[90mPressione Enter para finalizar o jogo...\033[0m")