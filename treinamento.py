from deepface import DeepFace
import os
import cv2

arquivo = open('dataset_apos_treino.txt', 'a')
arquivo.write('Nome                         Positivo     Negativo' + '\n')
arquivo.close()

origem = 'Banco Imagens'
diretorio = os.listdir(origem)

temFace = 0
naoTemface = 0

for imagem in diretorio:  
    # Abre o arquivo dataset_apos_treino.txt
    arquivo = open('dataset_apos_treino.txt', 'a')
    nome = imagem.split('-')[0]      
    # Carrega a imagem
    img = cv2.imread(origem + '/' + imagem)
    # Detecta a face na imagem
    detectors = ["opencv", "ssd", "mtcnn", "dlib", "retinaface"]
    face = DeepFace.detectFace(img, detector_backend = detectors[4], enforce_detection = False)
    if face.all() != 0: 
        
        print('Face detectada')

        if len(nome) == 1:
            arquivo.write(imagem + '              1            0' + '\n')
            
        elif len(nome) == 2:
            arquivo.write(imagem + '            1            0'+'\n')
            
        elif len(nome) == 3:
            arquivo.write(imagem + '          1            0' + '\n')

        arquivo.close()
            
    else:

        print('Não há face') 

        if len(nome) == 1:           
            arquivo.write(imagem + '              0            1' + '\n')
            
        if len(nome) == 2:
            arquivo.write(imagem + '            0            1' + '\n')
            
        elif len(nome) == 3:
            arquivo.write(imagem + '          0            1' + '\n')



                

