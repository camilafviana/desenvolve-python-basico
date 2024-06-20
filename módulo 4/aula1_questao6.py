n=int(input())
cont=0
soma_sapo,soma_rato,soma_coelho= 0,0,0

while cont <n:
    quantia=int(input())
    tipo= input()
    if tipo=='s': 
        soma_sapo += quantia
    elif tipo== 'r':
        soma_rato+= quantia
    elif tipo=='c': 
        soma_coelho+= quantia

    cont+=1

    print("total de cobaias:", soma_sapo+soma_rato+soma_coelho)
    print("total de sapos:", soma_sapo)
    print("total de ratos:", soma_rato)
    print("total de coelhos:", soma_coelho)
