dic = {"continentes": {"test01.txt":[(1, 14),(1,25)], "test02.txt":[(1, 13),(2,25)], "test03.txt":[(1, 10),(3,40)]}}

print(dic)
finDato, iteradorDato =False, ''
finDocumento, iteradorDocumento, documentoActual = False, '', ''
#finPalabra, iteradorPalabra =False, ''


def Dato(palabra, documento):
  global iteradorDato,finDato
  if (iteradorDato == ''):
    iteradorDato = iter(dic[palabra][documento])
  try:
    dato = iteradorDato.__next__()
    print(f"{palabra} encontrada en {documento} en la fila y columna {dato}")
    finDato = False
  except StopIteration:
    print("FinDato")
    finDato = True
    Documento(palabra)

def Documento(palabra):
  global iteradorDocumento,finDocumento, documentoActual,finDato,iteradorDato
  if (iteradorDocumento == ''):
    iteradorDocumento = dic[palabra].keys().__iter__()
    documentoActual = iteradorDocumento.__next__()
  try:
    if(finDato):
      iteradorDato = ''
      documentoActual = iteradorDocumento.__next__()
      
    Dato(palabra,documentoActual)
    finDocumento = False
  except StopIteration:
    finDocumento = True
  
    
Documento("continentes")
print('--------------')
Documento("continentes")
print('--------------')
Documento("continentes")
print('--------------')
Documento("continentes")
print('--------------')
Documento("continentes")
print('--------------')
Documento("continentes")
