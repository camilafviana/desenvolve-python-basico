#entrada
distancia= float(input("qual a distância em km?"))
peso= float(input("qual o peso em kg?"))

#processamento
if distancia <=100:
    valor_kg=1.00

elif 101<= distancia <=300:
    valor_kg=1.50
else: valor_kg=2.00

frete= valor_kg*peso

if peso>10:
    frete+=10
print (f"o valor do frete é: R${frete:,2}")