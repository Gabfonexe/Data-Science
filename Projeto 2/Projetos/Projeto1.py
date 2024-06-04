import PyPDF2
import os

mesclar = PyPDF2.PdfMerger

lista_arquivos = os.listdir("arquivos_PDF")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
  if ".pdf" in arquivo:
    mesclar.append(f'Arquivos / {arquivo}')

mesclar.write('PDF final.pdf')




