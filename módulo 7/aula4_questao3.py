with open('estomago.txt', 'r', encoding='utf-8') as file:
    linhas = file.readlines()

print("Primeiras 25 linhas do arquivo:")
for linha in linhas[:25]:
    print(linha.strip())
num_linhas = len(linhas)
print(f"\nNúmero de linhas no arquivo: {num_linhas}")
linha_mais_longa = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres: {linha_mais_longa.strip()}")
contagem_nonato = sum(1 for linha in linhas if 'nonato' in linha.lower())
contagem_iria = sum(1 for linha in linhas if 'íria' in linha.lower() and 'iria' not in linha.lower())
print(f"\nMenções ao personagem 'Nonato': {contagem_nonato}")
print(f"Menções ao personagem 'Íria': {contagem_iria}")