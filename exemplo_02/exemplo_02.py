from operator import truediv

idade = 20
possui_carteira = True

resultado = idade >= 18 and possui_carteira
print(resultado)

# not
# Inverte o resultado e uma condição

aluno_matriculado = True
print(not aluno_matriculado)

# 2. Operadores de comparação

print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
print(idade <= 18)

# 3. Estrutura if

idade = 18

if idade >= 18:
    print("Maior de idade")

# 4. Estrutura if / else

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")