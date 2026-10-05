frases_iniciais = ["Primeiro registro no meu diário.\n",
    "Hoje aprendi a manipular arquivos em Python.\n",
    "O modo 'w' sobrescreve o arquivo se ele já existir.\n",]
with open("diario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(frases_iniciais)
print("3 frases gravadas com sucesso!")
novas_frases = ["Adicionando um novo pensamento ao final do dia.\n",
    "O modo 'a' preserva o conteúdo anterior sem apagá-lo.\n",]
with open("diario.txt", "a", encoding="utf-8") as arquivo:
    arquivo.writelines(novas_frases)
print("Mais 2 frases adicionadas com sucesso!")
nome_arquivo = "diario.txt"
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    print(f"--- Conteúdo de {nome_arquivo} ---\n")
    for indice, linha in enumerate(arquivo, start=1):
        # .strip() remove a quebra de linha extra ao imprimir
        print(f"{indice}. {linha.strip()}")