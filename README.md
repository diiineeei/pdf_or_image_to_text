##Instalando Dependências (Ubuntu)
#####Primeiro vamos começar pela instalação do Tesseract OCR. Abra o terminal e digite o seguinte comando:

> sudo apt-get install tesseract-ocr tesseract-ocr-por
#####Também precisamos instalar a biblioteca Pillow e suas dependências. Ela será necessária para carregar a imagem para nosso script:

#####Ubuntu 12.04/14.04:

> sudo apt-get install python-dev python3-dev build-essential liblcms1-dev zlib1g-dev libtiff4-dev libjpeg8-dev libfreetype6-dev libwebp-dev
> pip install Pillow
#####Ubuntu 15.04/15.10/16.04:

> sudo apt-get install python-dev python3-dev build-essential liblcms2-dev zlib1g-dev libtiff5-dev libjpeg8-dev libfreetype6-dev libwebp-dev
> pip install Pillow
#####Agora partiremos para a instalação do wrapper que irá permitir a utilização do Tesseract através do python:

> pip install pytesseract

#####por ultimo a instalação do pdf2image para converter pdfs em imagens através do python:
> pip install pdf2image