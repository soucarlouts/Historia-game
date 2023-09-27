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
armas = None
acessorios = None


def rolar_dado():
    return random.randint(1, 6)
resultado_dados = rolar_dado()
pygame.init()

pygame.mixer.music.load("C:\Historia-game\Som\drusila_audiogame.mp3")

pygame.mixer.music.load("somdefase.mp3")
pygame.mixer.music.load("drusila_audiogame.mp3")

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



texto = '''\033[91m

 _|       ██████╗ ██████╗ ██╗   ██╗███████╗██╗██╗      █████╗        _|
 _|       ██╔══██╗██╔══██╗██║   ██║██╔════╝██║██║     ██╔══██╗       _|
 _|_/     ██║  ██║██████╔╝██║   ██║███████╗██║██║     ███████║     _/_|   
 _|_/     ██║  ██║██╔══██╗██║   ██║╚════██║██║██║     ██╔══██║     _/_|
 _|_/_/   ██████╔╝██║  ██║╚██████╔╝███████║██║███████╗██║  ██║   _/_/_|
 _|_/_/_/ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝ _/_/_/_|
                          (rpg text game)\n
                   Um mundo mágico de imaginação,
                com textos que prendem seus jogadores
                    e exploram suas capacidades!\033[91m\n'''

velocidade = 0.010
fade_in_text(texto, velocidade)

texto = "\n\033[90mPressione Enter para começar o jogo...\033[0m"
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
input()
pygame.mixer.music.stop()
pygame.quit()
clear_screen()

texto = ('\033[93mAncião\033[0m: Oh Olá, como estás nobre viajante? diga me, o que tu procuras? aventura? diversão? batalhas, ouro, gloria?  HAHAHAHAHA!!!\n\033[93mAncião\033[0m: Veremos como você se sairá nessas terras traiçoerais, luta, conquiste e saqueie, mostre a este lugar maldito e agourento do que você é feito,\n\033[93mAncião\033[0m: Mostre o que corre dentro de tua pele, mostre-nos que cor é seu sangue se tu tiveres coragem para tentar, se tiver o peito e alma de um guerreiro de verdade não tera duvidas ao mostrar ao continente de drusila quem é você e o que você é HAHAHAHAHA!!!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.06)
time.sleep(pause)

clear_screen()

print('''\033[92m 
 █████╗     ███████╗██╗      ██████╗ ██████╗ ███████╗███████╗████████╗ █████╗ 
██╔══██╗    ██╔════╝██║     ██╔═══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗
███████║    █████╗  ██║     ██║   ██║██████╔╝█████╗  ███████╗   ██║   ███████║
██╔══██║    ██╔══╝  ██║     ██║   ██║██╔══██╗██╔══╝  ╚════██║   ██║   ██╔══██║
██║  ██║    ██║     ███████╗╚██████╔╝██║  ██║███████╗███████║   ██║   ██║  ██║
╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
 \033[92m''')
pygame.init()
pygame.mixer.music.load("C:\Historia-game\Som\somdefase.mp3")
pygame.mixer.music.play()
input('\n\033[90mpróximo...\033[0m')
clear_screen()

texto = ('\033[93mNarrador\033[0m: A grande floresta de drusila, que contem as grandes árvores frutiferas, belas e perfumadas, é um labirinto gigante, a unica forma de realmente conhecer esta floresta,\n\033[93mNarrador\033[0m: é morando ou caçando aqui e isso é mostrado pelos ēlifi nome dos nativos élficos da floresta, aqui caçam, pescam, e plantam suas árvores, são seres esguios e dificeis de localizar, mas ja foram avistados colhendo suas frutas')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.06) 
time.sleep(pause)

texto = ('\n\033[93mNarrador\033[0m: A floresta tem um ecossistema proprio, místico e abriga varias raças diferentes, Os ēlifis aqui nascidos,\neram criados como gados para o abate, e essa pratica foi mantida por mais de 3 séculos, os ēlifi ao decorrer desses anos criaram um ódio pelos humanos, que no momento, não pode ser simplesmente esquecido...')
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
pygame.mixer.music.load("somdefase.mp3")
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

texto = ('\033[95mGarota\033[0m: E o que tu és,',nome,'?\n')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
input()

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

texto = ('\n\033[95mGarota\033[0m: o senhor não se lembra de nada?')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[94mVocê\033[0m: Não...')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[95mGarota\033[0m: Bom, por enquanto, vamos lavar essas roupas e limpar seus ferimentos, você esta na pior...')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[94mVocê\033[0m: Quem é você, e por quê esta me ajudando?')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[95mGarota\033[0m: sou apenas uma garota do campo, o ajudei pois senti que era a coisa certa a se fazer.')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[94mVocê\033[0m: O-Obrigado...')
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

texto = (f'\033[93mNarrador\033[0m: Você pega seu/a {armas} e limpa com cautela, à marcas e arranhões, mas você segue em frente...\n')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)

texto = (f'\033[93mNarrador\033[0m: Você equipa seu/a {acessorios} e reflete como tudo isso aconteceu, mas tudo estava tão confuso que você só seguiu ao banheiro para se limpar sem dar muita atenção...\n')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = (f'\033[93mNarrador\033[0m: A mulher estrangeira lava suas vestimentas enquanto você se limpava, quando saiu de seu banho achou suas vestimentas limpas, porem no estado que estavam, eram apenas trapos, e somente por pouco lembrava sua forma antiga. Mas voce não se lembra do que aconteceu, com apenas seu/a {armas} e {acessorios} voce decide agradecer a mulher estrangeira e partir para tentar descobrir o que aconteceu, mas antes voce à pede para lhe mostrar onde o achou.')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause2)

texto = ('\n\033[95mGarota\033[0m: Bom, depois dessa longa caminhada no bosque só posso lhe trazer até aqui. Boa sorte guerreiro, que a luz de \033[4mThalmor\033[0m brilhe sobre ti!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = (f'\n\033[93mNarrador\033[0m: E assim começa sua jornada, com apenas seu/a {armas} em mãos e trapos em seu corpo você decide investigar...')
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
texto = ("\n\033[90mPressione Enter para começar a primeira fase...\033[0m")
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
input()
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
        texto = "\n\033[93mNarrador\033[0m: Subir de Nível? "
        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)

        opcao_xp = input().upper()

        if opcao_xp == "NAO":
            time.sleep(pause)
            texto = ("\033[93mNarrador\033[0m: Você armazenou o XP!")
            for letra in texto:
                print(letra, end='', flush=True)
                time.sleep(0.05)
            break
        elif opcao_xp == "SIM":
            time.sleep(pause)
            texto = ("\033[93mNarrador\033[0m: Você subiu de nível!")
            for letra in texto:
                print(letra, end='', flush=True)
                time.sleep(0.05)
            break
        else:
            time.sleep(pause)
            print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
            continue
    else:
        print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
        opcao_fome = input("\n\033[93mNarrador\033[0m: você esta com fome, deseja comer? ").upper()

time.sleep(pause)
clear_screen()

texto = ('\033[93mNarrador\033[0m: você olha e caminha mais um pouco ao seu redor e vê marcas de batalha nas árvores o que parecem ser garras, com grandes árvores dilaceradas em volta, você investiga!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = (f'\n\033[93mNarrador\033[0m: enquanto você olha as árvores, ouve pegadas se aproximando, é algo grande! Você saca sua/seu {armas} e logo em seguida ouve um grunido que faz seu peito resonar com medo!') 
pygame.init()
pygame.mixer.music.load("Bear growl.ogg")
pygame.mixer.music.play()
texto = (f'\n\033[93mNarrador\033[0m: e um enorme urso ensanguentado pula de fora da floresta, em sua pelagem densa à marcas de espadas apenas olhar para tal criatura o enche de medo...')
pygame.mixer.music.stop()
pygame.quit()
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)

#BATALHA
texto = "\n\033[93mNarrador\033[0m: Atacar? "
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
opcao_batalha= input().upper()
while True:
    if opcao_batalha == "NAO":
        time.sleep(pause)
        texto = ('\033[93mNarrador\033[0m: Seu coração se enche de medo, suas mãos tremulas seguram sua arma com falta de confiança, o urso caminha para o atacar mas acaba se distraindo com um barulho alto na floresta e sai rugindo e correndo...\n')
        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
        break
    elif opcao_batalha == "SIM":
        texto = ("\033[93mNarrador\033[0m: Mesmo com medo você tem fé em si mesmo agarra a sua arma com o próprio coração e ataca!")
        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(0.05)
        time.sleep(pause)
        if resultado_dados > 1:
            print('\n\033[93mNarrador\033[0m: Sucesso no ataque, você matou o urso!')
            print(letra, end='', flush=True)
            time.sleep(0.05)
            break
        else:
            print('\033[93mNarrador\033[0m: O grande urso desvia de seu ataque, porem ao desviar bate a cabeça em uma árvore, e fica inconsiente por um tempo...')
            print(letra, end='', flush=True)
            time.sleep(0.05)
            break
    else:
        print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
        continue

texto = ('\033[93mNarrador\033[0m: Neste mesmo instante uma bela e luminosa fada aparece acima de seus olhos e fala com você!')
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

texto = ('\033[93mNarrador\033[0m: Você segue as marcas de forma quase linear, conforme sua velocidade aumenta, seu coração acompanha seus pés com o peito acelerado, você tem medo do que pode encontrar, muito você ja corre, seus pensamentos embaralham e sua cabeça o tontea de confusão nao sabe o que vai achar, você nao sabe o que deve pensar, quem é você e por que estava na floresta, por que estava desacordado?')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = ('\n\033[93mNarrador\033[0m: voçê sente medo, seu estomago revira ao sentir o cheiro podre de carne, depois de andar em direção ao cheiro, você vê corpos dilacerados, armaduras que outrorá foram brilhantes e reluzentes, agora foscas e ensanguentadas, o sangue está seco, os corpos ja iniciaram a decomposição, por isso o cheiro, você tampa sua boca e nariz, o local está insuportavel...')
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
texto = ("\n\033[90mPressione Enter para começar a Segunda fase...\033[0m")
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)

input()
clear_screen() 

texto = ('\033[93mNarrador\033[0m: Uma coisa lhe chama atenção, um envelope de carta perto de um dos corpos, você pega? ')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
opcao_carta = input().upper()
while True:
    if opcao_carta == "NAO":
            time.sleep(pause)
            texto = ("\033[93mNarrador\033[0m: você não pega a carta...")
            for letra in texto:
                print(letra, end='', flush=True)
            time.sleep(0.05)
            break
    elif opcao_carta == "SIM":
            time.sleep(pause)

            texto = ("\033[93mNarrador\033[0m: você se agacha perto de um dos corpos e pega o envelope, ele esta vazio, porém não é um envelope comum, a marca de cera, você a reconhece, é da realeza Drusiana!")
            for letra in texto:
                print(letra, end='', flush=True)
            time.sleep(0.05)
            break
    else:
            time.sleep(pause)
            print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
            continue

texto = ('\n\033[93mNarrador\033[0m: após isso, voçê ve repara em algo muito incomum, em uma das carcaças, você ve aquilo que se asemelha a uma seta você investiga? ')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
opcao_seta = input().upper()
while True:
    if opcao_seta == "NAO":
            time.sleep(pause)
            texto = ("\033[93mNarrador\033[0m: Você não pega a seta, porem consegue ouvir o som de uma das arvores gemendo e rangendo, uma árvore viva se revela, você nao tem escolha se não lutar...")
            for letra in texto:
                print(letra, end='', flush=True)
            time.sleep(0.05)
            break
    elif opcao_seta == "SIM":
            time.sleep(pause)
            texto = ("\n\033[93mNarrador\033[0m: Novamente, você se abaixa e pega até então a desconhecida seta, parece uma flecha comum, mas você não à reconhece de lugar algum. você a guarda, logo após consegue ouvir o som de uma das árvores gemendo e rangendo, uma árvore viva se revela, você não tem escolha se não lutar...")
            for letra in texto:
                print(letra, end='', flush=True)
            time.sleep(0.05)
            break
    else:
            time.sleep(pause)
            print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
            continue
        
texto = ('você chega mais perto da árvore e a cada passo ela fica maior, mas você à enfrenta sem exitar!')
for letra in texto:
            print(letra, end='', flush=True)
time.sleep(0.05)
