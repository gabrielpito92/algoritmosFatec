num = int(input('digite um número inteiro: '))

resultado = num % 5
resultado2 = num % 3

if(resultado == 0 and resultado2 == 0):
    print('FizzBuzz')
else:
    print(num)