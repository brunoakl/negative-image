# Autores: Bruno Machado Ferreira e Ernani Mendes da Fonseca Neto
## Projeto Python para aplicar filtro negativo em imagem cinza

Testado com
- Ubuntu 20.04
- Conda 4.12.3
- Python 3.7.8


### Instalando dependências(Conda, OpenCV, matplotlib e auxiliares)
- $ conda create -n vc
- $ conda env list
- $ conda activate vc
- $ conda install scikit-image opencv
- $ pip install matplotlib
- $ pip install scikit-image
- $ sudo apt-get install libopencv-*
- $ pip install opencv-contrib-python
- $ conda update -n base -c defaults conda

### Explicação
Ambos os scripts funcionam adequadamente, porém o v1.py contém um parâmetro estático para receber a imagem, lendo qualquer imagem nomeada como "exemplo.jpg".

Já o v2.py não tem esse problema, pois fizemos uso da biblioteca argparse.ArgumentParser que nos permitiu criar um parâmetro flexível, 
permitindo o código ler imagem com outros nomes a partir do parâmetro -i. No fim das contas, v2.py é o código com funcionamento mais completo.


### Executando
- $ conda activate vc
- $ python v1.py (Lê somente a imagem exemplo.jpg)
- $ python v2.py -i dino.jpg

### Resultados esperados
Após o processamento, deverá apresentar 3 imagens:
> A versão original mais duas resultantes(a versão cinza e a versão negativa).
> Depois, as imagens resultantes serão salvas em disco, na pasta postprocessing.
> Cada processamento substituirá as imagens da tentativa anterior, em ambos os códigos.
