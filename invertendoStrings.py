"""
Invertendo Strings
Crie um programa que recebe uma string e imprime ela de trás para frente.

Exemplo:
Entrada: "Python"
Saída: "nohtyP"
"""

string = input("Informe uma palavra que deseja inverter: ")

inverter_palavra = ''.join(reversed(string))
print(f"Palavra invertida: {inverter_palavra}")