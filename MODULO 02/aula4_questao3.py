# Q3 - Calcula o preço total de uma compra com 3 produtos

# Inicializa o preço total
total = 0

# Loop para três produtos
for i in range(1, 4):
    # Solicita o nome do produto
    nome = input(f"Digite o nome do produto {i}:")
    
    # Solicita o preço unitário do produto
    preco = float(input(f"Digite o preço unitário do produto {i}:"))
    
    # Solicita a quantidade do produto
    quantidade = int(input(f"Digite a quantidade do produto {i}: "))
    
    # Calcula o subtotal do produto e adiciona ao total
    total += preco * quantidade

# Imprime o total formatado com separador de milhar e duas casas decimais
print(f"Total: R${total:,.2f}")
