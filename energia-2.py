etotal=0

arq= open('dados_energia.txt','a')
for i in range(0,5):
  edia= input()
  edia=float(edia)
  edia*=0.624
  arq.write('dia')
  arq.write(str(i+1))
  arq.write(':\t')
  arq.write(str(edia))
  arq.write(' R$')
  arq.write('\n')
  etotal+=edia
arq.write('valor total:')
arq.write(str(etotal))
arq.write(' R$')
arq.close
print (etotal)