
# Substituindo Caracteres
# Solicite ao usuário que digite uma frase e substitua todas as vogais por "*".
#
# Exemplo:
# Entrada: "Python é incrível"
# Saída: "Pyth*n *ncr*v*l"

frase = "Python é incrível"
n_letras = str.maketrans("aeiou", "*****")
n_texto = frase.translate(n_letras)
print(n_texto)