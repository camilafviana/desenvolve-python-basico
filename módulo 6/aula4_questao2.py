frase = input("Digite uma frase: ")

vogais = [char for char in frase if char.lower() in 'aeiou']
print("Vogais:", sorted(vogais))  # Ordenando alfabeticamente

consoantes = [char for char in frase if char.isalpha() and char.lower() not in 'aeiou']
print("Consoantes:", consoantes)