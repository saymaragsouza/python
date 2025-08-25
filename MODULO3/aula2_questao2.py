# Questão 2
# Entrada permitida se pelo menos uma das duas for maior de idade

idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

pode_entrar = idade_juliana > 17 or idade_cris > 17
print(pode_entrar)
