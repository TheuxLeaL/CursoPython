#Crie um algoritmo que leia um número e mostra o seu dobro, triplo e raiz quadrada
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}'.format(n,d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {}.'.format(n, t, n, r))