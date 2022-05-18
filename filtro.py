import os

# Acessar o diretorio Banco Imagens
origem = 'Banco Imagens'
diretorio = os.listdir(origem)

arquivo = open('dataset_sem_treino.txt', 'w')
arquivo.write('Nome                         Positivo     Negativo')

for imagem in diretorio:
    # Pegar o nome da imagem e salvar no arquivo txt dataset_sem_treino.txt
    nome = imagem.split('-')[0]
    # Se o id da imagem for de 1 a 400 colocar o 1 em Negativo
    if int(nome) <= 400:
        if len(nome) == 1:
            arquivo.write('\n' + imagem + '              0            1')
        elif len(nome) == 2:
            arquivo.write('\n' + imagem + '            0            1')
        elif len(nome) == 3:
            arquivo.write('\n' + imagem + '          0            1')
                
    elif int(nome) > 400:
        if len(nome) == 1:
            arquivo.write('\n' + imagem + '              1            0')
        elif len(nome) == 2:
            arquivo.write('\n' + imagem + '            1            0')
        elif len(nome) == 3:
            arquivo.write('\n' + imagem + '          1            0')
    


            
    