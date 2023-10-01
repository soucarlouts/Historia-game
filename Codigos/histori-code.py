import time
import random
import os
import pygame

class Arma:
    def __init__(self, dano, ataque):
        self.dano = dano
        self.ataque = ataque

    def get_dano(self):
        return self.dano

    def get_ataque(self):
        return self.ataque

EspadaTal = Arma("Ataque Corte!!!" , 10)
pause = 1.0
pause2 = 2.0
pause3 = 3.0
pause4 = 10.0
armas = None
acessorios = None


def rolar_dado():
    return random.randint(1, 6)
resultado_dados = rolar_dado()
pygame.init()
pygame.mixer.music.load("Historia-game/som_unis.mp3")
pygame.mixer.music.load("Historia-game/somdefase.mp3")
pygame.mixer.music.load("Historia-game/drusila_audiogame.mp3")
pygame.mixer.music.play()

def fade_in_text(texto, velocidade):
    for i in range(len(texto)):
        print(texto[i], end='', flush=True)
        time.sleep(velocidade)

#90m cinza
#91m vermelho
#92m verde
#93m amarelo
#94m azul
#95m roxo
#96m azul claro
#97m branco

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

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
pygame.mixer.music.load("Historia-game/som_unis.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
time.sleep(pause2)

clear_screen()

pygame.init()
pygame.mixer.music.load("Historia-game/drusila_audiogame.mp3")
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

texto = ('\033[93mAncião\033[0m: Oh Olá, como estás nobre guerreiro? diga-me, o que tu procuras? aventura? diversão? batalhas? ouro ou gloria? HAHAHAHAHA!!!\n\033[93mAncião\033[0m: Veremos como você se sairá nessas terras traiçoeiras, lute, conquiste e saqueie, mostre a este lugar maldito e agourento do que você é feito\n\033[93mAncião\033[0m: Mostre o que corre dentro de tua pele, a cor de seu sangue se tu tivéres coragem para tentar, se tiver o peito e alma de um guerreiro de verdade não tera dúvidas ao mostrar ao continente de drusila quem é você e o que você é HAHAHAHAHA!!!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.06)
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
pygame.mixer.music.load("Historia-game/somdefase.mp3")
pygame.mixer.music.play()
input('\n\033[90mpróximo...\033[0m')
clear_screen()

texto = ('\033[93mNarrador\033[0m: A grande floresta de drusila, que contem as grandes árvores frutiferas, belas e perfumadas, é um labirinto gigante, a única forma de realmente conhecer esta floresta, é morando ou caçando aqui e isso é mostrado pelos ēlifi nome dos nativos élficos da floresta, aqui caçam, pescam, e plantam suas árvores, são seres esguios e dificeis de localizar, mas ja foram avistados colhendo suas frutas.')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.06) 
time.sleep(pause)

texto = ('\n\033[93mNarrador\033[0m: A floresta tem um ecossistema próprio, místico e abriga várias raças diferentes, os ēlifis aqui nascidos eram criados como porcos para o abate, e essa prática foi mantida por mais de 3 séculos, os ēlifis ao decorrer desses anos criaram um ódio pelos humanos, que no momento, não pode ser simplesmente esquecido...')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.06) 
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
pygame.mixer.music.load("Historia-game/somdefase.mp3")
pygame.mixer.music.play()
input('\n\033[90mpróximo...\033[0m')
clear_screen()

texto = ('\033[95mGarota\033[0m: Oh! Finalmente, você despertou está machucado e essas vestimentas, Ough! fedem, e muito!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05) 
time.sleep(pause)

texto = ('\n\033[95mGarota\033[0m: Diga-me qual é o teu nome? ')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
nome = input()
time.sleep(pause)

texto = (f'\033[95mGarota\033[0m: Pelo que vejo em suas vestimentas parece que servia o exército de drusila, mas qual classe você era, {nome}?\n')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)

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

texto = ('\033[95mGarota\033[0m: Ah, mas é claro, com essas vestimentas era óbvio!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = (f'\n\033[95mGarota\033[0m: o que fazes aqui {nome}?')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[94mVocê\033[0m: Eu... eu não me lembro.')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[95mGarota\033[0m: o senhor não se lembra de nada? nada mesmo?')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[94mVocê\033[0m: Só lembro de saber quem sou, mas não de estar aqui, agora...')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

clear_screen()

texto = ('\n\033[95mGarota\033[0m: Bom, por enquanto, vamos lavar essas vestimentas e limpar seus ferimentos, você esta na pior...')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[94mVocê\033[0m: Quem é você, e por quê esta me ajudando?')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[95mGarota\033[0m: sou apenas uma garota do campo, o ajudei pois senti que era a coisa certa a se fazer...')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[94mVocê\033[0m: O-Obrigado, eu agradeço pela serventia...')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[95mGarota\033[0m: bom, agora que estás indo se limpar, pegue seus equipamentos e armas e dê um trato neles pois estão bem imundos!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

clear_screen()

def obter_armas_e_acessorios(classe):
    match classe:
        case "Paladino":
            return "Espada", "Armadura"
        case "Feiticeiro":
            return "Cajado", "Amuleto"
        case "Arqueiro":
            return "Arco", "Aljava"
        case _:
            return "Classe não reconhecida", "Acessórios não disponíveis"

classe_escolhida = classes
armas, acessorios = obter_armas_e_acessorios(classe_escolhida)

texto = (f'\033[93mNarrador\033[0m: Você pega seu/sua {armas} e limpa com cautela, à marcas e arranhões, mas você segue em frente...\n')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)

texto = (f'\033[93mNarrador\033[0m: Você ajusta seu/sua {acessorios} e reflete como tudo isso aconteceu, mas tudo estava tão confuso que você só seguiu ao banheiro para se limpar sem dar muita atenção...\n')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = (f'\033[93mNarrador\033[0m: A mulher estrangeira lava suas vestimentas enquanto você se limpava, quando saiu de seu banho achou suas vestimentas limpas, porem no estado que estavam, eram apenas trapos, e somente por pouco lembrava sua forma antiga. Mas voce não se lembra do que aconteceu, com apenas seu/sua {armas} e {acessorios} voce decide agradecer a mulher estrangeira e partir para tentar descobrir o que aconteceu, mas antes voce à pede para lhe mostrar onde o achou.')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause2)

clear_screen()

texto = ('\033[95mGarota\033[0m: Bom, depois dessa longa caminhada no bosque só posso lhe trazer até aqui. Boa sorte guerreiro, que a luz de \033[4mThalmor\033[0m brilhe sobre ti!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = (f'\n\033[93mNarrador\033[0m: E assim começa sua jornada, com apenas seu/sua {armas} em mãos e trapos em seu corpo você decide investigar...')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
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
pygame.mixer.music.load("Historia-game/somdefase.mp3")
pygame.mixer.music.play()
texto = ("\n\033[90mPressione enter para começar a primeira fase...\033[0m")
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.03) 
input()
pygame.mixer.music.stop()
pygame.quit()
clear_screen()          
      

texto = ('\033[93mNarrador\033[0m: você está na entrada de uma floresta cercada por árvores frutiferas, suas frutas são de cores variadas, e exalam o melhor perfume que seu nariz ja sentiu!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = "\n\033[93mNarrador\033[0m: você esta com fome, deseja comer? "
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)

opcao_fome = input().upper()
while True:
    if opcao_fome == "NAO":
        time.sleep(pause)

        texto = ("\033[93mNarrador\033[0m: Você decide seguir em frente...")
        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
        break
    elif opcao_fome == "SIM":
        time.sleep(pause)

        texto = ("\033[93mNarrador\033[0m: você pega uma fruta estranha, aparência de maçã, porém com coloração de madeira. Você a morde, seu suco e sabor o revigoram.")
        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
        break

    print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
    opcao_fome = input("\n\033[93mNarrador\033[0m: você esta com fome, deseja comer? ").upper()

time.sleep(pause)

clear_screen()

texto = ('\033[93mNarrador\033[0m: Você olha e caminha mais um pouco ao seu redor e vê marcas de batalha nas árvores o que parecem ser garras, com grandes árvores dilaceradas em volta, você investiga!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = (f'\n\033[93mNarrador\033[0m: Enquanto você olha as árvores, ouve pegadas se aproximando, é algo grande! Você saca sua/seu {armas} e logo em seguida ouve um grunido que faz seu peito resonar com medo!') 
pygame.init()
pygame.mixer.music.load("Historia-game/som_urso.mp3")
pygame.mixer.music.play()
texto = (f'\n\033[93mNarrador\033[0m: e um enorme urso ensanguentado pula de fora da floresta, em sua pelagem densa à marcas de espadas apenas olhar para tal criatura o enche de medo...')
pygame.mixer.music.stop()
pygame.quit()
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
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
pygame.mixer.music.load("Historia-game/somdefase.mp3")
pygame.mixer.music.play()
texto = ("\n\033[90mPressione enter para começar a batalha...\033[0m")
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.03) 
input()
pygame.mixer.music.stop()
pygame.quit()

clear_screen()   

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
P2 = Personagem("\033[91mUrso ensanguentado\033[0m", 80, 15)

while P1.pv > 0 and P2.pv > 0:
    tipo_ataque_escolhido = input(f"\033[93mNarrador\033[0m: Escolha seu ataque (\033[92mataque direto\033[0m/\033[92mataque rápido\033[0m/\033[92mataque pesado\033[0m) para {P1.nome}: ")
    
    if tipo_ataque_escolhido in ataques_disponiveis:
        P1.atacar(P2, tipo_ataque_escolhido)
    else:
        print("\033[93mNarrador\033[0m: Tipo de ataque escolhido não está disponível. Digite novamente. ")
        continue
    
    tipo_ataque_monstro = random.choice(list(ataques_disponiveis.keys()))
    P2.atacar(P1, tipo_ataque_monstro)

    if P1.pv <= 0:
        print(f"\n\033[93mNarrador\033[0m: {P1.nome} foi derrotado")
        break
    elif P2.pv <= 0:
        print(f"\n\033[93mNarrador\033[0m: {P2.nome} foi derrotado")
        break

time.sleep(pause)
clear_screen()

texto = ('\n\033[93mNarrador\033[0m: Neste mesmo instante uma bela e luminosa fada aparece acima de seus olhos e fala com você!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

clear_screen()

texto = ('\033[95mFada\033[0m: Por sorte nesta grande batalha os deuses tiveram piedade de você guerreiro, pois vi suas ações e não esta nada bom para enfrentar as criaturas maléficas desta terra, não se acostume com milagres, pois este lugar é traiçoeiro!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[93mNarrador\033[0m: Ao adentrar a floresta você vê um labirinto de árvores, você mal entrou e ja se sente perdido tendo apenas as marcas de garra nas árvores, o som ominoso que você ouve ja é o suficiente para sentir o mau agouro que lhe espera porem, você deve prosseguir, afinal, não é como se lhe sobrasse muita escolha...')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

clear_screen()

texto = ('\033[93mNarrador\033[0m: Você segue as marcas de forma quase linear, conforme sua velocidade aumenta, seu coração acompanha seus pés com o peito acelerado. você tem medo do que pode encontrar, seus pensamentos embaralham e sua cabeça o tontea de confusão, você não sabe o que vai achar, ver e encontrar po este lugar maldito...')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[93mNarrador\033[0m: Você sente medo, ao adentrar a floresta você sente um cheiro podre de carne, depois de andar em direção ao cheiro, você vê corpos dilacerados, armaduras que outrorá foram brilhantes e reluzentes, agora foscas e ensanguentadas, o sangue está seco, os corpos ja iniciaram a decomposição, por isso o cheiro, você tampa sua boca e nariz, o local está insuportavel...')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
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
pygame.mixer.music.load("Historia-game/somdefase.mp3")
pygame.mixer.music.play()
texto = ("\n\033[90mPressione enter para começar a Segunda fase...\033[0m")
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.03) 
input()
pygame.mixer.music.stop()
pygame.quit()
clear_screen() 

texto = ('\033[93mNarrador\033[0m: Uma coisa lhe chama atenção, um envelope de carta perto de um dos corpos, você pega? ')

for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)

opcao_carta = input().upper()

while True:
    if opcao_carta == "NAO":
        time.sleep(pause)
        texto = ("\033[93mNarrador\033[0m: Você não pega a carta...")
        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
        break
    elif opcao_carta == "SIM":
        time.sleep(pause)
        texto = ("\033[93mNarrador\033[0m: Você se agacha perto de um dos corpos e pega o envelope. Ele está vazio, porém não é um envelope comum; a marca de cera, você a reconhece, é da realeza Drusiliana!")
        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
        break
    else:
        time.sleep(pause)
        print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
        continue

texto = ('\n\033[93mNarrador\033[0m: Após isso, você repara em algo muito incomum, em uma das carcaças, você vê aquilo que se assemelha a uma seta, Você investiga? ')

for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)

opcao_seta = input().upper()

while True:
    if opcao_seta == "NAO":
        time.sleep(pause)
        texto = ("\033[93mNarrador\033[0m: Você não pega a seta, porém consegue ouvir o som de uma das árvores gemendo e rangendo. Uma árvore viva se revela, você não tem escolha senão lutar...")
        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
        break
    elif opcao_seta == "SIM":
        time.sleep(pause)
        texto = ("\033[93mNarrador\033[0m: Novamente, você se abaixa e pega até então a desconhecida seta, parece uma flecha comum, mas você não a reconhece de lugar algum. Você a guarda, logo após consegue ouvir o som de uma das árvores gemendo e rangendo. Uma árvore viva se revela, você não tem escolha senão lutar...")
        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
        break
    else:
        time.sleep(pause)
        print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
        continue

texto = ('\n\033[93mNarrador\033[0m: Você chega mais perto da árvore e a cada passo ela fica maior, mas você a enfrenta sem hesitar!')
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
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
pygame.mixer.music.load("Historia-game/somdefase.mp3")
pygame.mixer.music.play()
texto = ("\n\033[90mPressione enter para começar a batalha...\033[0m")
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.03) 
input()
pygame.mixer.music.stop()
pygame.quit()

clear_screen() 

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
P2 = Personagem("\033[91mÁrvore viva\033[0m", 80, 15)

while P1.pv > 0 and P2.pv > 0:
    tipo_ataque_escolhido = input(f"\033[93mNarrador\033[0m: Escolha seu ataque (\033[92mataque direto\033[0m/\033[92mataque rápido\033[0m/\033[92mataque pesado\033[0m) para {P1.nome}: ")
    
    if tipo_ataque_escolhido in ataques_disponiveis:
        P1.atacar(P2, tipo_ataque_escolhido)
    else:
        print("\033[93mNarrador\033[0m: Tipo de ataque escolhido não está disponível. Digite novamente. ")
        continue
    
    tipo_ataque_monstro = random.choice(list(ataques_disponiveis.keys()))
    P2.atacar(P1, tipo_ataque_monstro)

    if P1.pv <= 0:
        print(f"\n\033[93mNarrador\033[0m: {P1.nome} foi derrotado")
        break
    elif P2.pv <= 0:
        print(f"\n\033[93mNarrador\033[0m: {P2.nome} foi derrotado")
        break
time.sleep(pause3)
clear_screen()

texto =('\033[93mNarrador\033[0m: Depois de batalhar com Árvore viva, você vê um homem assustado indo em sua direção, você para e tenta entender o que está acontecendo')
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[92mHomem desconhecido\033[0m: Obrigado senhor por nos salvar dessa maligna e maldita árvore viva, ela assombrava e aterrorizava nosso vilarejo á décadas, depois que o rei de drusila parou de enviar seus soldados para nos apoiar tudo desabou!')
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[94mVocê\033[0m: Mas como assim parou de enviar soldados para cá? a missão e a vontade dele era sempre sevir e proteger todos os vilarejos e o reino dele, porque parar assim do nada?')
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[92mHomem desconhecido\033[0m: Eu também gostaria de saber nobre guerreiro mas o que está acontecendo por agora no reino esta afetando tudo e a todos...')
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

clear_screen()

texto = ('\033[93mNarrador\033[0m: você se assusta ao saber o que está acontecendo no reino, pois você não se lembra de quase nada, mas mesmo assim agora sente que tem um propósito e uma misão para seguir! ')
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[93mNarrador\033[0m: Você agora decide ir seguir uma longa viagem até o reino de Drusila para ver o que está acontecendo e porque o rei está sendo tão mal com seu povo...')
for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)
