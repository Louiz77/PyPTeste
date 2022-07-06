import random
import turtle
import os
from time import sleep
fin = 0
lv = turtle.getscreen()
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
placar_pone = 0
placar_ptwo = 0
figura = 0
while fin == 0:
    t = turtle.Turtle()
    """
    t.goto(100,100)
    t.goto(130,200)
    t.home()
    t.goto(100,100)
    t.goto(130,200)
    """
    """
    t.goto(100,100)
    t.circle(20)
    t.end_fill()
    t.home()
    c = t.clone()
    t.color("magenta")
    c.color("red")
    t.circle(100)
    c.circle(60)
    """
    player_one = turtle.Turtle()
    player_one.color("green")
    player_one.shape("turtle")
    player_one.penup()
    player_one.goto(-200,100)
    player_two = player_one.clone()
    player_two.color("blue")
    player_two.penup()
    player_two.goto(-200,-100)

    die = [1,2,3,4,5,6]

    for i in range(20):
        if player_one.pos() >= (300,100):
            print("\n---------------------\n1 venceu!")
            print("Jogador 1: ")
            placar_pone = placar_pone + 1
            print(placar_pone)
            print("\nJogador 2: ")
            print(placar_ptwo)
            skk = turtle.Turtle()
            turtle.forward(100)
            turtle.right(60)
            turtle.forward(100)
            turtle.right(60)
            turtle.forward(100)
            turtle.right(60)
            turtle.forward(100)
            turtle.right(60)
            turtle.forward(100)
            turtle.right(60)
            turtle.forward(100)
            figura = figura + 1
            sleep(2)

            """
            finalizar = input('Finalizar programa ?\n1. Sim\n2. Nao\n')
            if finalizar == '1':
                fin = 1
            if finalizar == '2':
                print('Aguarde!\n')
                cls()
                sleep(1)
                continue
            """
            break
        elif player_two.pos() >= (300,-100):
            print("\n---------------------\n2 venceu!")
            print("Jogador 1: ")
            print(placar_pone)
            print("\nJogador 2: ")
            placar_ptwo = placar_ptwo + 1
            print(placar_ptwo)
            turtle.forward(100)
            turtle.right(60)
            turtle.forward(100)
            turtle.right(60)
            turtle.forward(100)
            turtle.right(60)
            turtle.forward(100)
            turtle.right(60)
            turtle.forward(100)
            turtle.right(60)
            turtle.forward(100)
            figura = figura + 1
            sleep(2)
            """
            finalizar = input('Finalizar programa ?\n1. Sim\n2. Nao\n')
            if finalizar == '1':
                fin = 1
            if finalizar == '2':
                print('Aguarde!\n')
                cls()
                sleep(1)
                continue
            """
            break
        else:
            if figura == 6:
                if placar_pone > placar_ptwo:
                    print("\nJOGADOR 1 CAMPEAO!!")
                if placar_ptwo > placar_pone:
                    print("\nJOGADOR 2 CAMPEAO!!")
                sleep(1)
                turtle.clear()
                turtle.circle(90)
                turtle.clear()
                figura = 0
                placar_pone = 0
                placar_ptwo = 0
            player_one_turn = input("\nJogador 1: Rodar dados")
            die_outcome = random.choice(die)
            print("\nNumeros dos dados: ")
            print(die_outcome)
            print("Passos: ")
            print(20*die_outcome)
            player_one.fd(20*die_outcome)
            player_two_turn = input("\nJogador 2: Rodar dados")
            die_outcome = random.choice(die)
            print("\nNumeros dos dados: ")
            print(die_outcome)
            print("Passos: ")
            print(20*die_outcome)
            player_two.fd(20*die_outcome)
    """
    finalizar = input('Finalizar programa ?\n1. Sim\n2. Nao\n')
    if finalizar == '1':
        fin = 1
    if finalizar == '2':
        print('Aguarde!\n')
        cls()
        sleep(1)
        continue
    """
