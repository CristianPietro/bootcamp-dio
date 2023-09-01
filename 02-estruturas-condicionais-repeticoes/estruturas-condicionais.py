MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input('Informe sua idade: '))

#EXEMPLO COM IF

if idade >= MAIOR_IDADE:
    print("maior de idade, pode tira a CNH.")

if idade < MAIOR_IDADE:
    print("Menor de idade, não pode tirar a CNH")

#EXEMPLO COM IF e ELSE

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Menor de idade, ainda não pode tirar a CNH.")


#EXEMPLO COM IF e ELIF e ELSE

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Menor de idade, ainda não pode tirar a CNH.")