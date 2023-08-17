# Autores: Bruno Machado Ferreira(181276) e Ernani Neto(180914)
# Criado para a atividade de Imagem Negativa no Classroom	



# Bibliotecas utilizadas

import cv2
import matplotlib.pyplot as plt
import skimage.io

#Recebe a imagem
image = cv2.imread('exemplo.jpg')

#Converte a original para cinza	
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
skimage.io.imsave('./postprocessing/cinza.jpg', gray)


#Converte a cinza para negativa
negative = cv2.imread("./postprocessing/cinza.jpg")
  
# get height and width of the image
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

#Exibe as imagens
cv2.imshow('Original',image)
cv2.imshow('Cinza', gray)
cv2.imshow('Negativa', negative)

#Espera uma ação para fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()


