# Questão 1
# Juliana e Cris só podem entrar no bar se ambas forem maiores de 17 anos

idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

pode_entrar = idade_juliana > 17 and idade_cris > 17
print(pode_entrar)
