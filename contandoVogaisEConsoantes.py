# Contando Vogais e Consoantes
# Receba uma palavra ou frase e conte quantas vogais e quantas consoantes existem nela.
#
# Exemplo:
# Entrada: "programacao"
# Saída: Vogais: 5, Consoantes: 6

def contar_vogais_consoantes(frase): # Definição da Função
    vogais = "aeiouAEIOU" # Definimos uma string contendo todas as vogais maiúsculas e minúsculas.
    num_vogais = sum(1 for c in frase if c in vogais) # Contando as Vogais
    num_consoantes = sum(1 for c in frase if c.isalpha() and c not in vogais) # Contando as Consoantes

    return num_vogais, num_consoantes # Retornando os Valores


frase = (input("Digite uma frase ou palavra: ")) # Define uma frase ou palavra para testar a função
vogais, consoantes = contar_vogais_consoantes(frase) # Chama função e armazena valores
print(f"Vogais: {vogais}, Consoantes: {consoantes}") # Imprime na tela
