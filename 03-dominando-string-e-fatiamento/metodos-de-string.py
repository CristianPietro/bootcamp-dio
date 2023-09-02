nome = "CrisTiaN"

print(nome.upper()) # Tudo maiúsculo
print(nome.lower()) # Tudo minúsculo
print(nome.title()) # Primeira letra maiúsculo

texto = "   Olá mundo!"

print(texto)
print(texto.strip()) # Remove os espaços
print(texto.rstrip()) # Remove os espaços da direita
print(texto.lstrip()) # Remove os espaços da esquerda

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print("-".join(menu))