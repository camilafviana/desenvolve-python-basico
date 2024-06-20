def calcular_notas(valor):
    # Definindo as denominações das notas
    notas = [100, 50, 20, 10, 5, 2, 1]
    
    # Lista para armazenar a quantidade de cada nota
    quantidade_notas = []
    
    # Calculando a quantidade de cada nota
    for nota in notas:
        quantidade = valor // nota  # Quantidade de notas do valor atual
        quantidade_notas.append(quantidade)  # Armazenando a quantidade
        valor -= quantidade * nota  # Subtraindo o valor correspondente à quantidade de notas
        
    # Exibindo o resultado
    for i in range(len(notas)):
        print(f"{quantidade_notas[i]} nota(s) de R${notas[i]},00")

# Exemplo de uso:
valor = int(input("Digite um valor em reais: "))
calcular_notas(valor)