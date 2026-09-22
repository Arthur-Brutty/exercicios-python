soma = 0 

while True:
    numero = float(input("Digite um numero (ou 0 para sair ): "))
    if numero == 0:
        break
    soma += numero
    print("Soma atual:", soma)