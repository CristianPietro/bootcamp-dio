texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end="")

print()

# RANGE com FOR

for numero in range(0,11):
    print(numero, end="")

#EXIBINDO A TABUADA DO 5

for numero in range(0, 51, 5):
    print(numero)