while True:
    perg = int(input('De qual número você deseja ver a tabuada?'))
    if perg < 0:
        print('\033[1;32mPrograma de tabuada encerrado, volte sempre!\033[m')
        break
    for multiplicadores in range(1,11):
        res = perg * multiplicadores
        print(f'{perg} X {multiplicadores} = {res}')