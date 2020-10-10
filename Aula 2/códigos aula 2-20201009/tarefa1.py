# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
#Pedindo para o Usuário inserir o número
num=input("Insira o número de 5 dígitos:\n")

#Conferindo se o número de dígitos é igual a 5
while len(num) != 5:
    print("O número digitado não tem 5 digitos, por favor digite novamente.")
    num = str(input("Insira o número de 5 digitos:\n"))

#Separando os dígitos do número
num = int(num)

quinto = num % 10  # pega o quinto numero
num = num // 10    # retira o ultimo; num agora tem 4 digitos
primeiro = num // 1000  # pega o primeiro 
num = num % 1000  # retira o primeiro digito; num agora tem 3 digitos
segundo = num // 100  # pega o segundo digito (agora o primeiro)
quarto = num % 10   # pega o ultimo digito

#Verificando se o número digitado é palindrome
if primeiro==quinto and segundo==quarto:
    print("O número digitado é palindrome.")
else:
    print("O número não é palindrome.")
