# Q2 - Converte Fahrenheit em Celsius

# Solicita ao usuário a temperatura em Fahrenheit
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Converte para Celsius usando a fórmula C = (F - 32) * 5/9
celsius = int((fahrenheit - 32) * (5 / 9))

# Imprime a temperatura convertida
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")
