#Autores: Bruno Machado Ferreira(181276) e Ernani Neto(180914)

# Bibliotecas utilizadas
from argparse import ArgumentParser
from skimage import io
import skimage
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte, random_noise
from skimage import data
from skimage import filters
import cv2
import numpy as np
import cv2 as cv
from scipy import ndimage
import matplotlib.pyplot as plt
import os


# Lê os parâmetros passados na linha de comando
parser = ArgumentParser()
parser.add_argument("-i", "--imagem", default="exemplo.jpg",
                    help="Imagem a ser processada")
parser.add_argument("-ig", "--interface", default="sim",
                    help="Parâmetro do suavizador. Depende do tipo do ruído")

args = parser.parse_args()

# Mostra os parâmetros lidos
print("Executando sequência com")
print("Imagem  = ",args.imagem)
print("Interface Gráfica = ",args.interface)

# Abre a imagem de entrada
original = io.imread(args.imagem)

# Converte imagem colorida para cinza
gray = rgb2gray(original)
skimage.io.imsave('./postprocessing/cinza.jpg', gray)

#Converte a cinza para negativa
negative = cv2.imread("./postprocessing/cinza.jpg")
  
#Obter medidas e ler pixel a pixel
height, width, _ = negative.shape
  
for i in range(0, height - 1):
    for j in range(0, width - 1):
          
        # Get the pixel value
        pixel = negative[i, j]
          
        # Negate each channel by 
        # subtracting it from 255
          
        # 1st index contains red pixel
        pixel[0] = 255 - pixel[0]
          
        # 2nd index contains green pixel
        pixel[1] = 255 - pixel[1]
          
        # 3rd index contains blue pixel
        pixel[2] = 255 - pixel[2]
          
        # Store new values in the pixel
        negative[i, j] = pixel

skimage.io.imsave('./postprocessing/negativa.jpg', negative)

# Mostra as imagens finais
if args.interface == "sim":

  fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(8, 4),sharex=True, sharey=False)

  ax = axes.ravel()

  ax[0].imshow(original)
  ax[0].axis('off')
  ax[0].set_title('Original')

  ax[1].imshow(gray,cmap='gray')
  ax[1].axis('off')
  ax[1].set_title('Cinza')
  
  ax[2].imshow(negative,cmap='gray')
  ax[2].axis('off')
  ax[2].set_title('Negativa')


  fig.tight_layout()

  fig.canvas.manager.set_window_title('Resultados para imagem '+args.imagem)
  plt.show()
