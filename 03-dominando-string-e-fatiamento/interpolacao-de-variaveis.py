nome = "Pietro"
idade = 27
profissao = "desempregado"
linguagem = "python"
saldo = 45.435

dados = {"nome": "Pietro", "idade": 27}

print("nome: %s idade: %s" % (nome, idade))

print("nome: {} idade: {}".format(nome, idade))
print("nome: {0} idade: {1}".format(nome, idade))

print("nome: {nome} idade: {idade}".format(nome=nome, idade=idade))
print("nome: {name} idade: {age} {name} {age} {name}".format(name=nome, age=idade))
print("nome: {nome} idade: {idade}".format(**dados))

print(f"nome: {nome} idade: {idade}")
print(f"nome: {nome} idade: {idade} Saldo: {saldo: 10.2f}")
print(f"nome: {nome} idade: {idade} Saldo: {saldo: .2f}")