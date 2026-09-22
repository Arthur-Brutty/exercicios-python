quantidade_positivos = 0
while True:
    numero = float(input("Digite um numero (ou 0 para sair):"))
    if numero == 0:
        break
    if numero > 0:
        quantidade_positivos += 1
        print("Quantidade de numeros positivos:", quantidade_positivos)