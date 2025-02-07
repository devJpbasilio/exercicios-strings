"""
Verificando Palíndromos
Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma de frente para trás.
Escreva um programa que verifica se uma palavra é um palíndromo.

Exemplo:
Entrada: "radar"
Saída: "É um palíndromo"
"""

def palindrome(string):
    string = string.lower()
    string_invertida = ''.join(reversed(string))
    if string == string_invertida:
        print(f"Palavra invertida: {string_invertida}")
        return True
    else:
        print(f"Palavra invertida: {string_invertida}")
        return False

print("Verificando Palíndromos\n")
word = input("Digite uma palavra: ")

if palindrome(word):
    print("\nA palavra é um Palíndromo.")
else:
    print("\nA palavra não é um Palíndromo")