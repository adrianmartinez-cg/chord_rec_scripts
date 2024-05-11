import os

pasta = os.path.join(os.getcwd(),'pop909_expected')

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.txt'):
        parte_numerica = nome_arquivo.split('_')[0]
        try:
            novo_nome = f"{parte_numerica}.lab"
            caminho_antigo = os.path.join(pasta, nome_arquivo)
            caminho_novo = os.path.join(pasta, novo_nome)
            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado {nome_arquivo} para {novo_nome}")
        except ValueError:
            print(f"Pulando {nome_arquivo} (não está no formato esperado)")

print("Renomeação de arquivos concluída.")