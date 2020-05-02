from random import randint, choice
import os
import random

def senha_simples(tam, num):
    for _ in range(tam - num):
        r = choice([(65,90), (97, 122)])
        senha.append(chr(randint(*r)))

    for _ in range(num):
        senha.append(randint(0,9))
    
    random.shuffle(senha)
    return print(''.join(map(str,senha)))

def senha_pro(tam, num, spec):
    for _ in range(tam - num):
        r = choice([(65,90), (97, 122)])
        senha.append(chr(randint(*r)))

    for _ in range(num):
        senha.append(randint(0,9))
    
    for _ in range(spec):
        spc = choice([(33,47), (58,64)])
        senha.append(chr(randint(*spc)))

    random.shuffle(senha)
    return print(''.join(map(str,senha)))

tam = 0
while tam < 6:
    tam = int(input("Determine o tamanho da sua senha, no mínimo 6 caractéres: "))

    if tam >= 6:
        op = str(input("Você deseja caractéres especiais na sua senha? S/N"))


        senha = []


        if op == 'N' or op == 'n':
            letras = randint(1, tam)
            num = tam - letras
            os.system('clear')
            print("SENHA GERADA:")
            senha_simples(tam,num)
        elif op == 'S' or op == 's':
            letras = randint(1, tam//2)
            num = (tam-letras) //2
            spec = tam - letras - num
            os.system('clear')
            print('SENHA GERADA:')
            senha_pro(tam,num,spec)

