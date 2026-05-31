from math import hypot
import matplotlib.pyplot as plt

print('{:=^50}'.format(' Calculo da hipotenusa '))

cateto_o = float(input('Digite o valor do 1° cateto: '))
print()
cateto_a = float(input('Digite o valor do 2° cateto: '))

hipotenusa = hypot(cateto_o, cateto_a)
print(f'O valor da hipotenusa é de {hipotenusa:.2F}')
print('=' * 50)

x = [0, cateto_a, 0, 0]
y = [0, 0, cateto_o, 0]

plt.plot(x, y, 'b-', linewidth=2)
plt.fill(x, y, 'skyblue', alpha=0.3)

plt.text(cateto_a/2, -0.5, f'cateto adj. :{cateto_a}')
plt.text(-0.5, cateto_o/2, f'cateto op. :{cateto_o}', rotation=90)
plt.text(cateto_a/2, cateto_o/2, f'hipotenusa:{hipotenusa:.2f}', color='red')

plt.axis('equal')
plt.title("triangulo retângulo")
plt.show()