# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:20:16 2020

@author: João
Edit: Arthur Gini
"""

"""Simulating the dice game Craps."""
import random

#Declarando variaveis estatisticas
dados =[]

i=0
rodada=1
win =0 
loose =0

for i in range(1,10):

    def roll_dice():
        """Roll two dice and return their face values as a tuple."""
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        return (die1, die2)  # pack die face values into a tuple

    def display_dice(dice):
        """Display one roll of the two dice."""
        die1, die2 = dice  # unpack the tuple into variables die1 and die2
        print(f'Player rolled {die1} + {die2} = {sum(dice)}')

    def salvar():

        print(dados)

        if game_status == "WON": #se o status for win
            for i in enumerate(dados): #percorre dados
                if rodada == i: #se a rodada for i
                    dados.insert(rodada+1, win) #insere em rodada+1 a win

        elif game_status == "LOST": #se o status for win
            if rodada == i: #se a rodada for i
                dados.insert(rodada+1, loose) #insere em rodada+1 a win
        rodada = 1

        return print(list(dados))





    die_values = roll_dice()  # first roll
    display_dice(die_values)

    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)

    if sum_of_dice in (7, 11):  # win
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = 'LOST'
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        display_dice(die_values)
        sum_of_dice = sum(die_values)
        
        #add codigo
        rodada += 1

        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
            
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'

    # display "wins" or "loses" message
    if game_status == 'WON':
        print('Player wins')
        win +=1
        salvar()

    else:
        print('Player loses')
        loose +=1
        salvar()


    """Codigo velho


        #add codigo
        print("Rodada", rodada)
        
        win += 1
        dados.insert(rodada, str(rodada))
        dados.insert(rodada+1,win)
        print(dados)
        

        #add codigo
        print("Rodada", rodada)
        loose += 1
        dados.insert(rodada, str(rodada))
        dados.insert(rodada+2,loose)
"""        
