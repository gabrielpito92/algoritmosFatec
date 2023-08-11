nome=input('Digite seu nome: ')
print('Ola', nome, 'seja bem vindo a Fatec Ourinhos!')

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

dia=input('Digite o dia de nascimento: ')
mes=input('Digite o mês de nascimento: ')
ano=input('Digite o ano de nascimento: ')

print('voce nasceu no dia', dia, 'do mes', mes, 'no ano', ano)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

num1 = input('digite um numero: ')
num2 = input('digite outro numero: ')

soma = float(num1) + float(num2)

print('A soma dos dois numeros digitados e:', soma)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))

soma = num1 + num2
multiplica = num1 * num2
divisao = num1 / num2
subtracao = num1 - num2

print('soma:', soma, 'subtracao:', subtracao, 'multiplicacao:', multiplica, 'divisao:', divisao)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))

potencia = num1 ** num2
resto = num1 % num2
div_int = num1 // num2

print('potencia:', potencia, 'resto da divisao:', resto, 'divisao inteira:', div_int)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

num1 = int(input('digite um numero: '))

raiz_quad = num1 ** 1/2
raiz_cub = num1 ** 1/3

print('raiz quadrada:', raiz_quad, 'raiz cubica:', raiz_cub)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

nome=input('Digite seu nome: ')
print(f"Bem vindo {nome}!")
print( f"Bem vindo {nome:20}!")
print( f"Bem vindo {nome :>20}!")
print( f"Bem vindo {nome:<20}!")
print( f"Bem vindo {nome:^20}!")
print( f"Bem vindo {nome:=^20}!")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

num1 = int(input('digite a temperatura em fahrenheit: '))
celsius = (num1 - 32) * (5/9)
print('a temperatura em celsius e:', celsius)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))

x = -b/a

print("O valor de X é:", x)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

base = float(input('digite a base em metros: '))
altura = float(input('digite a altura em metros: '))

area = base * altura

print('A area do terreno em metros e:', area)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

cavalos = int(input('Digite o número de cavalos que o haras possui: '))

ferraduras = cavalos * 4

print('o numero de ferraduras necessarias e:', ferraduras)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

paes = float(input('digite a quantidade de paes: '))
broas = float(input('digite a quantidade de broas: '))

paes_total = paes * 0.12
broas_total = broas * 1.5
total = paes_total + broas_total
poupanca = total * 0.1

print('valor total vendido:', total, 'valor para guardar:', poupanca)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

nome = input('Digite o seu nome: ')
idade = int(input('digite a sua idade em anos: '))

dias_vividos = idade * 365

print(nome + ',', 'você já viveu', dias_vividos, 'dias')

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

gasolina = float(input('digite o preco do litro da gasolina: '))
dinheiro = float(input('valor que deseja comprar de gasolina: '))

litros = dinheiro / gasolina

print('voce abasteceu', litros, 'de gasolina.')

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

peso = float(input('digite o peso total do prato (em gr) de comida: '))

pagar = peso * 12

print('voce deve pagar: R$', pagar)