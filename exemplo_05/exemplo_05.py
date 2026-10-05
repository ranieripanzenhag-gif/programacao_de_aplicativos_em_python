# O que é uma função?

# Uma função é um bloco de código criado para realizar
# Uma determinada tarefa.
# Ela permite organizar e reutilizar código

#1. Criando uma função
#utilizar a palavra def para uma função

print("\n- 1. Criando uma função")

def saudacao01():
    print("Olá, seja bem vindo!")

saudacao01()

#2. Criando uma função com um parâmetro
print("\n- 2. Criando uma função com parâmetro")

#parâmetros permitem enviar informações para a função

def saudacao02(nome):
    print(f"olá {nome}, seja bem vindo!")

saudacao02("Arthur")

#3. Mais de um parâmetro
print("\n- 3. Mais de um parâmetro")

def apresentar(nome, idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Arthur", 67)

#4. função com calculo
print("\n- 4. Função com cálculo")

def somar(num1, num2):
    resultado = num1 + num2
    print(f"resultado: {resultado}")

somar(10, 5)

#5. retornando um valor
print("\n- 5. Retornando um valor")

def somar_e_rotornar(num1, num2):
    resultado = num1 + num2
    return resultado

valor_retornado = somar_e_rotornar(50, 100)
print(f"O valor retornado é: {valor_retornado}")

#6. Função com condição
print("\n- 6. Função com condição")

def maior_de_idade(idade):
    if idade > 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(maior_de_idade(16))

#7. Parâmetro com valor padrão
print("\n- 6. Função com valor padrão")

def saudacao03(nome = "aluno"):
    print(f"Olá {nome}, seja bem vindo!")

saudacao03()