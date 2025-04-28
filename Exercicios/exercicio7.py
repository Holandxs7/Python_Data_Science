# Solicita o numerador
numerador = float(input("Digite o numerador: "))

# Solicita o denominador
denominador = float(input("Digite o denominador (não pode ser 0): "))

# Verifica se o denominador é zero
if denominador == 0:
    print("Erro: o denominador não pode ser 0!")
else:
    # Realiza a divisão
    divisao = numerador / denominador
    # Exibe o resultado
    print(f"O resultado da divisão é: {divisao}")