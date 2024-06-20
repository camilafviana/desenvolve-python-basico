n=int(input("digite a quantidade de números:"))
maior=0
while n>0:
    x=int(input("digte um número:"))
    if x > maior:
        maior= x
    n-=1
print("o maior valor é:",maior)