
import os

# Instruções
print('Preencha os campos abaixo com os dados do paciente.', '\n')
print(' ')


# Solicita os valores 
nome = input('Nome do paciente: ') 
print(' ')

altura_str = input('Altura do paciente(m): ')
print(' ')

peso_str = input('Peso do paciente: ')
print(' ')



# Convertendo peso e altura para float
peso = float(peso_str)
altura = float(altura_str)

# Calculo
imc = peso / (altura * altura)

# Abaixo do peso
limite_inf_muito_abaixo = 17

# Abaixo do peso
limite_inf_abaixo = 17.5
limite_sup_abaixo = 18.5

# Peso saudavel
limite_inf_saudavel = 18.5
limite_sup_saudavel = 24.9

# Sobrepeso
limite_inf_sobrepeso = 24.9
limite_sup_sobrepeso = 30

# Obeso
limite_sup_obeso = 30



# Limpa a tela de saída
os.system('cls' if os.name == 'nt' else 'clear')



# Design de saída
print('                 ', nome)
print('-------------------------------------------')
print('Altura:', f'{altura:.2f}') 
print('Peso:', str(f'{peso:.1f}'), 'Kg')
print(f"Seu IMC é: {imc:.2f}")
print('-------------------------------------------')


# Muito abaixo do peso:
if limite_inf_muito_abaixo >= imc:
    print(nome,'esta muito abaixo do peso!!! ')

else: 
    print


# Abaixo do peso
if limite_inf_abaixo <= imc <= limite_sup_abaixo:
    print(nome,'esta abaixo do peso! ')

else: 
    print


# Peso saudavel
if limite_inf_saudavel <= imc <= limite_sup_saudavel:
    print(nome,'esta com o peso ideal!!!')

else:
    print


# Sobrepeso
if limite_inf_sobrepeso <= imc <= limite_sup_sobrepeso:
    print(nome,'esta acima do peso!')

else:
    print


# Obeso
if limite_sup_obeso <= imc: 
    print(nome,'esta muito acima do peso!!!')

else:
    print


# Linhas em branco 
print('\n' * 5)