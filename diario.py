frases_iniciais = ["Primeiro registro no meu diário.\n",
    "Hoje aprendi a manipular arquivos em Python.\n",
    "O modo 'w' sobrescreve o arquivo se ele já existir.\n",]
with open("diario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(frases_iniciais)
print("3 frases gravadas com sucesso!")
