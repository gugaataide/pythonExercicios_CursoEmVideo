peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura (em metros)?'))
imc = peso / altura.__pow__(2)
print('Seu imc é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está na faixa:\033[1;31mAbaixo do peso!\033[m')
elif imc >= 18.5 and imc < 25.0:
    print('Você está na faixa:\033[1;32mPeso ideal!\033[m')
elif imc >= 25.0 and imc < 30.0:
    print('Você está na faixa:\033[1;31Sobrepeso! \033[m')
elif imc >= 30 and imc <= 40:
    print('Você está na faixa:\033[1;31mObesidade! \033[m')
elif imc > 40:
    print('Você está na faixa:\033[1;31mObesidade morbida!\033[m')
