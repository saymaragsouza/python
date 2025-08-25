# Q1 - Calcula o valor de um terreno

# Solicita ao usuário o comprimento do terreno em metros
comprimento = int(input("Digite o comprimento do terreno (em metros): "))

# Solicita ao usuário a largura do terreno em metros
largura = int(input("Digite a largura do terreno (em metros): "))

# Solicita ao usuário o preço do metro quadrado
preco_m2 = float(input("Digite o preço do metro quadrado: "))

# Calcula a área do terreno
area_m2 = comprimento * largura

# Calcula o preço total do terreno
preco_total = preco_m2 * area_m2

# Imprime o resultado formatado com duas casas decimais
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")
