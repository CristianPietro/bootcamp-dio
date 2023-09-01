saldo = 1000
saque = 1500

status = "sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque!")