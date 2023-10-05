# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 para manipular arquivos PDF (PdfReader)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_PDFS = PASTA_RAIZ / 'pdf_ori'
PASTA_SECO = PASTA_RAIZ / 'pasta'

FILE_PDF = PASTA_PDFS / 'R20230929.pdf'
PASTA_SECO.mkdir(exist_ok=True)

relatorio = PdfReader(FILE_PDF)

page_0 = relatorio.pages[0]
image_0 = page_0.images[0]
#print(page_0.extract_text())
#print(image_0)

#with open(PASTA_SECO/image_0.name, 'wb') as file:
#    file.write(image_0.data)

writer = PdfWriter()
#writer.add_page(page_0)

#with open(PASTA_SECO/'page_0.pdf', 'wb') as file:
#    writer.write(file)

#with open(PASTA_SECO/'novo_pdf.pdf', 'wb') as file:
#    for page in relatorio.pages:
#        writer.add_page(page)
#    writer.write(file)

#for i, page in enumerate(relatorio.pages):
#    with open(PASTA_SECO/f'page_{i}.pdf', 'wb') as file:
#        writer.add_page(page)
#        writer.write(file)

files = [
    PASTA_SECO/'page_0.pdf',
    PASTA_SECO/'page_1.pdf'
    ]

merger = PdfMerger()

for file in files:
    merger.append(file)

merger.write(PASTA_SECO/'merged.pdf')
merger.close()

