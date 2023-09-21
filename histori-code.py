import time

pause = 1.5

print('G- Oh! Finalmente, você despertou está machucado e essas vestimentas, Ough! fedem, e muito!')
time.sleep(pause)
nome = input('G- Diga-me qual és teu nome?\n')
time.sleep(pause)
print('G- E, o que tu és?')

opcoes_validas = ['Paladino', 'Feiticeiro', 'Arqueiro']

while True:
    classes = input('Escolha uma classe (Paladino, Feiticeiro, Arqueiro): \n')

    classes = classes.capitalize()

    if classes in opcoes_validas:
        break
    else:
        print('Opção inválida. Por favor, escolha entre Paladino, Feiticeiro ou Arqueiro.')
        continue

print('G- Ah, mas é claro, com essas vestimentas era óbvio!')
time.sleep(pause)
print(f'G- o que fazes aqui {nome} ?')
time.sleep(pause)
print('N- eu... eu não me lembro.')
time.sleep(pause)
print('G- o senhor não se lembra de nada?')
time.sleep(pause)
print('N- não...')
time.sleep(pause)
print('G- Bom, por enquanto, vamos lavar essas roupas e limpar seus ferimentos, você esta na pior.')
time.sleep(pause)
print('N- Quem é você, e por quê esta me ajudando?')
time.sleep(pause)
print('G- sou apenas uma garota do campo, o ajudei pois senti que era a coisa certa a se fazer.')
time.sleep(pause)
print('N- O-Obrigado.')

opcoes_validas_armas = ['Cajado', 'Espada', 'Arco']

while True:
    classes = input('Escolha uma arma (Cajado, Espada, Arco): \n')

    armas = classes.capitalize()

    if armas in opcoes_validas_armas:
        break
    else:
        print('Opção inválida. Por favor, escolha entre Cajado, Espada ou Arco.')
        continue

opcoes_validas_acessorios = ['Amuleto', 'Armadura', 'Aljava']

while True:
    classes = input('Escolha um acessório (Amuleto, Armadura, Aljava): \n')

    acessorios = classes.capitalize()

    if acessorios in opcoes_validas_acessorios:
        break
    else:
        print('Opção inválida. Por favor, escolha entre Paladino, Feiticeiro ou Arqueiro.')
        continue

print(f'Narrador- A mulher estrangeira lava suas vestimentas enquanto você se limpava, quando saiu de seu banho achou suas vestimentas limpas, porem no estado que estavam, eram apenas trapos, e somente por pouco lembrava sua forma antiga.Mas voce não se lembra do que aconteceu, com apenas seu/a {armas} e {acessorios} voce decide agradecer a mulher estrangeira e partir para tentar descobrir o que aconteceu, mas antes voce à pede para lhe mostrar onde o achou.')
