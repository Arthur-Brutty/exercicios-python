numeros = [1, 2, 3, 4, 5]
maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
        print("O maior numero ate agora:", maior)