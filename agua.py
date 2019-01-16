atotal=0
consumo=0
def arquivo(adia):
  arq.write('dia')
  arq.write(str(i+1))
  arq.write(':\t')
  arq.write(str(adia))
  arq.write(' R$')
  arq.write('\n')
def cal(atotal,adia):
  valor1=(10-consumo+adia)*11.82
  valor2=(consumo-10)*26.81
  return valor1+valor2
arq= open('dados_agua.txt','a')
x=0
for i in range(0,5):
  adia= input()
  adia=float(adia)
  consumo+=adia
  if consumo>=10 and x==0:
    x=1
  if x==0:
    adia*=11.82
  elif x==1:
    adia=cal(consumo,adia)
    x=2
  else:
    adia*=26.81
  arquivo(adia)
  atotal+=adia
arq.write('valor total:')
arq.write(str(atotal))
arq.write(' R$')
arq.close
print (atotal)