from pathlib import Path

caminho_pasta = Path()

#print(caminho_pasta.absolute())
caminho_arquivo = Path(__file__)
#print(caminho_arquivo.parent)

pasta_teste = caminho_arquivo.parent / 'teste'
#print(pasta_teste)

caminho_arquivo = Path('/tmp') / 'teste.txt'
#arquivo = caminho_pasta.absolute() / 'teste.txt'
#arquivo.touch()
#arquivo.write_text('Olá Mundo!!')
#print(arquivo.read_text())
#arquivo.unlink()

#with caminho_arquivo.open('a+') as arq:
#    arq.write('Uma linha \n')
#    arq.write('Duas linhas \n')

caminho_pasta = Path('/tmp/pasta_teste')
#caminho_pasta.mkdir()

sub_pasta = caminho_pasta / 'sub_pasta'
#sub_pasta.mkdir()

arquivo_pasta = sub_pasta / 'teste.py'
#arquivo_pasta.touch()
#arquivo_pasta.write_text('print("Hello word")')

