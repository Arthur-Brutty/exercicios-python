numero = int(input("Digite um numero inteiro nao negativo:"))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
    print(f"Fatorial de {i} = {fatorial}")