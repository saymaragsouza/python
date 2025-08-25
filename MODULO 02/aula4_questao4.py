# Q4 - Calcula a menor quantidade de notas para um valor em reais

# Solicita ao usuário um valor em reais
valor = int(input())

# Lista com os valores das notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Para cada valor de nota, calcula quantas notas são necessárias
for nota in notas:
    qtd = valor // nota        # Número de notas
    valor = valor % nota       # Atualiza o valor restante
    print(f"{qtd} nota(s) de R${nota},00")
