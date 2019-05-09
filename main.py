# Importando o módulo pdf2image para converter pdf em imagem
from pdf2image import convert_from_path
# convertendo pdf em imagens
pages = convert_from_path('testes.pdf', 500)
# salvando paginas
for page in pages:
    page.save('out.jpg', 'JPEG')


# Importando o módulo Pillow para abrir a imagem no script
from PIL import Image
# Módulo para a utilização da tecnologia OCR
import pytesseract

# Extraindo o texto da imagem
print(pytesseract.image_to_string(Image.open('out.jpg')))

