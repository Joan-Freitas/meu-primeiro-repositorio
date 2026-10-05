pessoa = {
    "nome": "José",
    "idade": 63,
    "cidade": "Criciúma",
    "profissão": "Estudante"}
pessoa.update({"email": "jfreitas@gmail.com"})
print("Dicionário completo:")
print(pessoa)
print("\nDados da pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")