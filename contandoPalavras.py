"""
Contando Palavras
Peça ao usuário para digitar uma frase e conte quantas palavras existem nela.

Exemplo:
Entrada: "Eu gosto de programar"
Saída: 4 palavras
"""

frase = "Eu gosto de programar"
letras = frase.split()
print(len(letras))