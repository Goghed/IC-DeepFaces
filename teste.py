from charset_normalizer import detect
from deepface import DeepFace
import os
import cv2
import matplotlib.pyplot as plt

maiorZero = 0
igualZero = 0
faceDetectada = 0
faceNaoDetectada = 0

backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']

# Entrar no diretorio Banco Imagens e listar todas as imagens
caminho = [os.path.join('Banco Imagens', f) for f in os.listdir('Banco Imagens')]

for imagem in caminho:
    img = cv2.imread(imagem)
    detectar_face = DeepFace.detectFace(img, target_size = (224, 224), detector_backend = backends[4], enforce_detection=False)

    if detectar_face is not None:        

        








