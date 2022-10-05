times= ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians','Bragantino', 'fluminense', 'América-MG',
        'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá','Juventude', 'Grêmio',
        'Bahia', 'Sport', 'Chapecoense')
print('=' * 10, 'Brasileirão', '=' * 10)
for c in range(0, len(times)):
    print(f'{times[c]} está na {c + 1}° posição.')
print('-=-' * 10,'5 Primeiros times', '-=-' * 10)
for pm in range(0, 5):
    print(times[pm])
print('-=-' * 10,'4 Ultimos times', '-=-' * 10)
for ut in range (-4, 0):
    print(times [ut])
print('=' * 5,'Em ordem alfabética:', '=' * 5)
print(sorted(times))
print('=' * 5,'Em que posição está a chapecoense?', '=' * 5)
chap = times.index('Chapecoense')
print(f'{chap + 1}° posição')