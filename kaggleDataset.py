import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import os
import cv2
from PIL import Image

api = KaggleApi()
api.authenticate()

# Criar o diretorio dataset_training
if not os.path.exists('Banco Imagens'):
    os.makedirs('Banco Imagens')

# Baixar o dataset de Yale Faces e salvar em dataset_training
kaggle.api.dataset_download_files('asacxyz/ic-fatecitu', path='Banco Imagens', unzip=True)

# Acessar o diretorio Banco Imagens e listar todas as imagens
caminho = [os.path.join('Banco Imagens', f) for f in os.listdir('Banco Imagens')]

cont = 1

for caminhoImagem in caminho:
    
    if ".jpeg" in caminhoImagem:  
        nomeArquivo = os.path.splitext(caminhoImagem)[0]  
        imagem = Image.open(caminhoImagem).convert('RGB').save(nomeArquivo+'.'+'jpg')
        os.remove(caminhoImagem)        

    if ".jpg" in caminhoImagem:        
        imagem = cv2.imread(caminhoImagem)                    
        img = cv2.resize(imagem, (600, 600))
        cv2.imwrite(caminhoImagem, img)
        os.rename(caminhoImagem, os.path.join('Banco Imagens', str(cont)+'-treinamento'+str(cont)+'.jpg'))
        cont += 1
        # Crie o diretorio Faces Detectadas
    if not os.path.exists('Faces Detectadas'):
        os.makedirs('Faces Detectadas')
    # Crie o diretorio Sem Faces
    if not os.path.exists('Sem Faces'):
        os.makedirs('Sem Faces')
        
    



        