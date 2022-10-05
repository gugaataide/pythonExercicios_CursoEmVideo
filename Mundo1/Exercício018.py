import math
num = float(input('Digite o ângulo:'))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tg = math.tan(math.radians(num))
print('O seno desse ângulo é: {:.2f} \n O cosseno desse ângulo é: {:.2f} \n A tangente desse ângulo é: {:.2f}'.format(sen, cos, tg))
