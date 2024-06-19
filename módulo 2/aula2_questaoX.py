v1=5
v2=2
print(type(v1))
print(type(v2))
divisao= v1/v2
print(divisao)
print(type(divisao))

v1="o resultado é"
v2=10
v3=3.5
soma=v2+v3
print(type(v1))
print(type(v2))
print(type(v3))
print(type(soma))

v1=10
v2=20
print(v1)
print(v2)
aux = v2
v3=[v1, v2] = [v2, v1]
print(v3)

'''juros = 1.01
saldo = 500.0
rendimento1 = saldo * juros
rendimento2 = rendimento1 * juros
rendimento3 = rendimento2 * juros
print("Após 3 meses meu novo saldo é")
print(rendimento3)
'''
juros = 1.01
saldo = 500.0
print(saldo)
saldo = saldo * juros #505 rendimento1
print(saldo)
saldo = saldo * juros #rendimento2
print(saldo)
saldo = saldo * juros #rendimento3
print(saldo)

print(type(saldo))