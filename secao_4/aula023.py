import os
import shutil
from pathlib import Path
from zipfile import ZipFile

CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula023_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula023_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula023_descompactado'

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

def criar_arquivo(qtd, zip_dir):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as file:
            file.write(texto)

criar_arquivo(10, CAMINHO_ZIP_DIR)

with ZipFile(CAMINHO_COMPACTADO, 'w') as zip_file:
    print('Compactando arquivo!!')
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            zip_file.write(os.path.join(root,file), file)

with ZipFile(CAMINHO_COMPACTADO, 'r') as zip_file:
    print('Lendo arquivo compactado')
    for file in zip_file.namelist():
        print(file)

with ZipFile(CAMINHO_COMPACTADO, 'r') as zip_file:
    print('Descompactando arquivo')
    zip_file.extractall(CAMINHO_DESCOMPACTADO)
