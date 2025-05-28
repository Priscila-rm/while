time = input('Digite o nome do melhor time do Brasil: ')

while time != 'Gigante das colinas':
    time = input('Qual é o melhor time do Brasil? ')
    if time == 'Gigante das colinas':
        print('Você acertou! vai Clube das Resgatas Vasco de Gama!')
    else:
        print('Tente novamente!')