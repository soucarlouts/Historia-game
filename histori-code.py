import time
import random
import os
import curses

pause = 1.0
pause2 = 2.0
pause3 = 3.0
def rolar_dado():
    return random.randint(1, 6)
resultado_dados = rolar_dado()

#90m cinza
#91m vermelho
#92m verde
#93m amarelo
#94m azul
#95m roxo
#96m azul claro
#97m branco

def fade_in_text(texto, velocidade):
    for i in range(len(texto)):
        print(texto[i], end='', flush=True)
        time.sleep(velocidade)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

texto = '''\033[91m

██████╗ ██████╗ ██╗   ██╗███████╗██╗██╗      █████╗ 
██╔══██╗██╔══██╗██║   ██║██╔════╝██║██║     ██╔══██╗
██║  ██║██████╔╝██║   ██║███████╗██║██║     ███████║
██║  ██║██╔══██╗██║   ██║╚════██║██║██║     ██╔══██║
██████╔╝██║  ██║╚██████╔╝███████║██║███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝╚══════╝╚═╝  ╚═╝
                 (rpg text game)\033[91m\n
           Um mundo mágico de imaginação,
        com textos que prendem seus jogadores
            e exploram suas capacidades!\n'''

velocidade = 0.02

fade_in_text(texto, velocidade)
time.sleep(1)

input("\n\033[90mPressione Enter para começar o jogo...\033[0m")
clear_screen()

time.sleep(pause2)
texto = ('\033[95mGarota\033[0m: Oh! Finalmente, você despertou está machucado e essas vestimentas, Ough! fedem, e muito!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05) 
time.sleep(pause)

nome = input ('\n\033[95mGarota\033[0m: Diga-me qual é o teu nome? ')
time.sleep(pause)

print ('\033[95mGarota\033[0m: E o que tu és,',nome,'?\n')

opcoes_classes = ['Paladino', 'Feiticeiro', 'Arqueiro']

while True:
    texto = classes = input('Escolha uma classe \033[92m(Paladino, Feiticeiro, Arqueiro): \033[0m')

    classes = classes.capitalize()

    if classes in opcoes_classes:
        break
    else:
        print('Opção inválida. Por favor, escolha entre Paladino, Feiticeiro ou Arqueiro.')
        continue

texto = ('\n\033[95mGarota\033[0m: Ah, mas é claro, com essas vestimentas era óbvio!')
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

texto = ('\n\033[94mVocê\033[0m: O-Obrigado...\n')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)

opcoes_armas = ['Espada' ,'Cajado', 'Arco']

while True:
    classes = input('\nEscolha uma arma \033[92m(Espada, Cajado, Arco): \033[0m')

    armas = classes.capitalize()

    if armas in opcoes_armas:
        break
    else:
        print('Opção inválida. Por favor, escolha entre Espada, Cajado ou Arco.')
        continue

texto = (f'\n\033[93mNarrador\033[0m: Você pega seu/a {armas} e a limpa com cautela, à marcas e arranhões, mas você segue em frente...\n')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)

opcoes_acessorios = ['Armadura', 'Amuleto', 'Aljava']

while True:
    classes = input('\nEscolha um acessório \033[92m(Armadura, Amuleto, Aljava): \033[0m')

    acessorios = classes.capitalize()

    if acessorios in opcoes_acessorios:
        break
    else:
        print('Opção inválida. Por favor, escolha entre Paladino, Feiticeiro ou Arqueiro.')
        continue

texto = (f'\n\033[93mNarrador\033[0m: Você equipa seu/a {acessorios} e reflete como tudo isso aconteceu, mas tudo estava tão confuso que você só seguiu ao banheiro para se limpar sem dar muita atenção...\n')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = (f'\033[93mNarrador\033[0m: A mulher estrangeira lava suas vestimentas enquanto você se limpava, quando saiu de seu banho achou suas vestimentas limpas, porem no estado que estavam, eram apenas trapos, e somente por pouco lembrava sua forma antiga. Mas voce não se lembra do que aconteceu, com apenas seu/a {armas} e {acessorios} voce decide agradecer a mulher estrangeira e partir para tentar descobrir o que aconteceu, mas antes voce à pede para lhe mostrar onde o achou.')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

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
███████╗ █████╗ ███████╗███████╗     ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝    ███║
█████╗  ███████║███████╗█████╗      ╚██║
██╔══╝  ██╔══██║╚════██║██╔══╝       ██║
██║     ██║  ██║███████║███████╗     ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═╝ 
\033[91m\n''')
input("\n\033[90mPressione Enter para começar a primeira fase...\033[0m")
clear_screen()          
      

texto = ('\n\033[93mNarrador\033[0m: você esta na entrada de uma floresta cercada por árvores frutiferas, suas frutas sao de cores variadas, e exalam o melhor perfume que seu nariz ja sentiu.')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

opcao_fome = input("\n\033[93mNarrador\033[0m: você esta com fome, deseja comer? ").upper()
while True:
    if opcao_fome == "NAO":
        time.sleep(pause)

        print("\033[93mNarrador\033[0m: Você decide seguir em frente.")
        break
    elif opcao_fome == "SIM":
        time.sleep(pause)

        print("\033[93mNarrador\033[0m: você pega uma fruta estranha, aparência de maçã, porém com coloração de madeira. Você a morde, seu suco e sabor o revigoram.")
        opcao_xp = input("Subir de Nível? ").upper()

        if opcao_xp == "NAO":
            time.sleep(pause)
            print("\033[93mNarrador\033[0m: Você armazenou o XP!")
            break
        elif opcao_xp == "SIM":
            time.sleep(pause)
            print("\033[93mNarrador\033[0m: Você subiu de nível!")
            break
        else:
            time.sleep(pause)
            print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
            continue
    else:
        print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
        opcao_fome = input("Você está com fome, deseja comer? ").upper()
time.sleep(pause)
clear_screen()

texto = ('\033[93mNarrador\033[0m: você olha mais um pouco ao seu redor e vê marcas de batalha nas árvores o que parecem ser garras, com grandes árvores dilaceradas em volta, você investiga!')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)
time.sleep(pause)

texto = (f'\n\033[93mNarrador\033[0m: enquanto você olha as árvores, ouve pegadas se aproximando, é algo grande! Você saca sua/seu {armas} e logo em seguida ouve um grunido que faz seu peito resonar com medo! e um enorme urso ensanguentado pula de fora da floresta, em sua pelagem densa à marcas de espadas apenas olhar para tal criatura o enche de medo...')
for letra in texto:
    print(letra,end='', flush=True)
    time.sleep(0.05)

#BATALHA
opcao_batalha= input("\n\033[93mNarrador\033[0m: Atacar? ").upper()
while True:
    if opcao_batalha == "NAO":
        time.sleep(pause)
        print('\033[93mNarrador\033[0m: Seu coração se enche de medo, suas mãos tremulas seguram sua arma com falta de confiança, Mas você nao faz nada...')
        break
    elif opcao_batalha == "SIM":
        print("\033[93mNarrador\033[0m: Mesmo com medo você tem fé em si mesmo agarra a sua arma com o próprio coração e ataca!")
        time.sleep(pause)
        if resultado_dados > 2:
            print('\033[93mNarrador\033[0m: Sucesso no ataque, você matou o urso!')
            break
        else:
            print('\033[93mNarrador\033[0m: O grande urso o matou...')
            break
    else:
        print("\033[93mNarrador\033[0m: Opção inválida. Por favor, escolha entre 'SIM' ou 'NAO'.")
        continue
