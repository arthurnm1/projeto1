arq=open('anagrama.txt','r')
anagrama=arq.readlines()
k=0
palavra=['b','a','t','a','t','a']
def anag(palavra,i):
  texto=[]
  for l in i:
    texto.append(l)
  if len(texto)==len(palavra):
    for m in palavra:
      for n in texto:
        if m==n:
          texto.remove(n)
          print (palavra)
          print (texto)
          break 
  if texto==[]:
    return 1
  return 0
for i in anagrama:
  i=i.replace('\n','')
  k+=anag(palavra,i)
arq.close
print (k)
    
  