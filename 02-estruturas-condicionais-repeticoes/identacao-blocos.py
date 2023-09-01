def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado")
        print("Retire seu dinheiro na boca do caixa")
    
    print("Obrigado por ser nosso cliene, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f"Seu saldo é {saldo}")
    
sacar(500)
depositar(1000)
