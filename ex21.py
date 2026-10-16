# Exercício 21: Faixa etária

# Leitura da idade
idade = int(input("Digite a idade: "))

# Teste das faixas etárias na ordem correta
if idade < 0:
    print("Idade inválida")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")